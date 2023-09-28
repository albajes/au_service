# Generated by Django 4.2.2 on 2023-09-24 15:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('au_service', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='BList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bad_user', models.ManyToManyField(related_name='bad_user', to=settings.AUTH_USER_MODEL)),
                ('good_user', models.ManyToManyField(related_name='good_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
