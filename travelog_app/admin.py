from django.contrib import admin

from .models import diary, prefectures, cities, likes,areas,follows

admin.site.register(diary)
admin.site.register(prefectures)
admin.site.register(cities)
admin.site.register(areas)
admin.site.register(follows)
admin.site.register(likes)