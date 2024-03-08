from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField('ニックネーム', max_length=50, null="false")

    class Meta:
        verbose_name_plural = 'CustomUser'


    


