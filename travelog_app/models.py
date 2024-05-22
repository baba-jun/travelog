from django.db import models
from accounts.models import CustomUser


class prefectures(models.Model):
    prefecture_id = models.CharField(verbose_name='都道府県コード', null=False, blank=False, max_length=2, primary_key=True)
    prefecture_name = models.CharField(verbose_name='都道府県名', null=False, blank=False, max_length=4,unique=True)

    class Meta:
        verbose_name_plural = 'prefectures'

    def __str__(self):
        return self.prefecture_name  

class cities(models.Model):
    city_id = models.CharField(verbose_name='市区町村コード', null=False, blank=False, max_length=5, primary_key=True)
    city_name = models.CharField(verbose_name='市区町村名', null=False, blank=False, max_length=10)
    prefecture_id = models.ForeignKey(prefectures, verbose_name='都道府県コード', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.city_id
    
class areas(models.Model):
    area_name = models.CharField(verbose_name='エリア名', null=False, blank=False, max_length=50)
    prefecture_name = models.ForeignKey(prefectures, db_column="prefecture_name",to_field='prefecture_name',verbose_name='都道府県名', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.area_name

class diary(models.Model):
    user_id = models.ForeignKey(CustomUser, verbose_name='User_ID', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', null=False, blank=False, max_length=50)
    comment = models.TextField(verbose_name='コメント', null=False, blank=False, max_length=200)
    country = models.CharField(verbose_name='観光地の国', null=True, blank=True,  max_length=30)
    prefectures = models.ForeignKey(prefectures, verbose_name='都道府県', blank=True, null=True, on_delete=models.PROTECT)
    area = models.ForeignKey(areas, verbose_name='エリア', blank=True, null=True, on_delete=models.PROTECT)
    favorites = models.PositiveIntegerField(verbose_name='favorites', null=False, blank=False, default=0)
    post_image1 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    post_image2 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    post_image3 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    post_image4 = models.ImageField(verbose_name='投稿画像', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(verbose_name='updated_at', auto_now=True)

    class Meta:
        verbose_name_plural = 'diary'


class likes(models.Model):
    user_id = models.ForeignKey(CustomUser, verbose_name='User_ID', on_delete=models.PROTECT)
    diary_id = models.ForeignKey(diary, verbose_name='Diary_ID', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(verbose_name='updated_at', auto_now=True)

    class Meta:
        verbose_name_plural = 'likes'