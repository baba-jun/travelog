from django.urls import path

from . import views


app_name = 'travelog_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create_post/', views.CreatePostView.as_view(), name="create_post"),
    path('csv_upload/', views.upload_csv_data, name='csv_upload'),
    path('get_city_dropdown/', views.get_city_dropdown, name='get_city_dropdown'),
]