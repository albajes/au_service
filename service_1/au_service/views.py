from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, BList
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer, BListSerializer


class UserViewSet(ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegistrationViewSet(ViewSet):
    serializer_class = RegistrationSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        inf = {'email': request.data.get('email'), 'password': request.data.get('password')}
        ex_response = TokenObtainPairSerializer().validate(attrs=inf)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        response.set_cookie('access', ex_response['access'], httponly=True)
        response.set_cookie('refresh', ex_response['refresh'], httponly=True)
        return response


class BListViewSet(ModelViewSet):
    queryset = BList.objects.all()
    serializer_class = BListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        good_user = request.user.id
        if good_user == request.data['bad_user']:
            return Response('Вы не можете сами себя добавить в ЧС', status=status.HTTP_400_BAD_REQUEST)

        try:
            blist1 = BList.objects.filter(good_user=good_user, bad_user=request.data['bad_user'])
        except KeyError:
            return Response('Укажите поле "bad_user"', status=status.HTTP_400_BAD_REQUEST)

        if len(blist1) >= 1:
            blist1.delete()
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

        return Response('Успешно', status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(good_user=self.request.user)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def retrieve_blist(request, good_user, bad_user):
    instance = get_object_or_404(BList.objects.all(), good_user=good_user, bad_user=bad_user)
    serializer = BListSerializer(instance)
    return Response(serializer.data)
