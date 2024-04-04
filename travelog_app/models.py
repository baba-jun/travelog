from django.db import models
from accounts.models import CustomUser

class diary(models.Model):
    user_id = models.ForeignKey(CustomUser, verbose_name='User_ID', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', null=False, blank=False, max_length=50)
    comment = models.TextField(verbose_name='コメント', null=False, blank=False, max_length=200)
    country = models.CharField(verbose_name='観光地の国', null=True, blank=False, max_length=30)
    prefectures = models.CharField(verbose_name='都道府県', null=True, blank=False, max_length=30)
    city = models.CharField(verbose_name='市町村区', null=True, blank=False, max_length=30)
    likes = models.PositiveIntegerField(verbose_name='likes', null=False, blank=False, default=0)
    favorites = models.PositiveIntegerField(verbose_name='favorites', null=False, blank=False, default=0)
    post_image1 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    post_image2 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    post_image3 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    post_image4 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    updated_at = models.DateField(verbose_name='updated_at', auto_now=True)

    class Meta:
        verbose_name_plural = 'diary'

    def __str__(self):
        return self.title