from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'travelog_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('home/', views.HomeView.as_view(), name='Home'),
    path('profile_edit/<int:pk>', views.ProfileEditView.as_view(), name="profile_edit"),
    path('search/', views.diary_search_view, name="search"),
    path('create_post/', views.CreatePostView.as_view(), name="create_post"),
    path('delete_post/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('csv_upload/', views.upload_csv_data, name='csv_upload'),
    path('get_area_dropdown/', views.get_area_dropdown, name='get_area_dropdown'),
    path('like_for_diary/', views.like_for_diary, name='like_for_diary'),
    path('follow_user/<int:pk>', views.AddFollow, name='follow_user'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)