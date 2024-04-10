from django.contrib import admin

from .models import diary, prefectures, cities

admin.site.register(diary)
admin.site.register(prefectures)
admin.site.register(cities)