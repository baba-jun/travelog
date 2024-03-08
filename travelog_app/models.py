from django.db import models
from accounts.models import CustomUser

class PostImages(models.Model):
    file_path = models.CharField(verbose_name='File_Path', null=True, blank=False, max_length=200)

    class Meta:
        verbose_name_plural = 'PostImages'

    def __str__(self):
        return self.created_at

class diary(models.Model):
    user_id = models.ForeignKey(CustomUser, verbose_name='User_ID', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='title', null=False, blank=False, max_length=50)
    comment = models.CharField(verbose_name='comment', null=False, blank=False, max_length=200)
    country = models.CharField(verbose_name='country', null=True, blank=False, max_length=30)
    prefectures = models.CharField(verbose_name='prefectures', null=True, blank=False, max_length=30)
    city = models.CharField(verbose_name='city', null=True, blank=False, max_length=30)
    likes = models.PositiveIntegerField(verbose_name='likes', null=False, blank=False, default=0)
    favorites = models.PositiveIntegerField(verbose_name='favorites', null=False, blank=False, default=0)
    post_images = models.ForeignKey(PostImages, verbose_name='Post_Img', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'diary'

    def __str__(self):
        return self.title