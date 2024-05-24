from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    display_name = models.CharField(verbose_name='ニックネーム', null=False, blank=False, max_length=20, default='ユーザー')
    profile_img = models.ImageField(verbose_name='プロフィール画像', blank=True, null=True, default='user.png')
    user_bio = models.CharField(verbose_name='プロフィール', null=True, blank=True, max_length=20, default='プロフィールです')

    class Meta:
        verbose_name_plural = 'CustomUser'

