from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RegistrationViewSet, LoginViewSet, BListViewSet, UserViewSet, RetrieveBlist

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'registration', RegistrationViewSet, basename='registration')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'blist', BListViewSet, basename='blist')

urlpatterns = [
    path('', include(router.urls)),
    path('ac_token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('re_token', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='verify'),
    path('get_blist/<int:good_user>/<int:bad_user>', RetrieveBlist.as_view(), name='get_blist')
]
