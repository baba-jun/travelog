from django.contrib import admin

from .models import CustomUser
from travelog_app.models import diary, PostImages

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(diary)
admin.site.register(PostImages)
