# Generated by Django 4.2.2 on 2023-09-24 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('au_service', '0004_delete_blist'),
    ]

    operations = [
        migrations.CreateModel(
            name='BList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bad_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bad_user', to=settings.AUTH_USER_MODEL)),
                ('good_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='good_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
