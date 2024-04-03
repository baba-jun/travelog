from django.urls import path

from . import views


app_name = 'travelog_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create_post/', views.CreatePostView.as_view(), name="create_post"),
]