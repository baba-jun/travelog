from django import forms
from .models import diary
 
class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = diary
        fields = ('user_id', 'title', 'comment', 'country', 'prefectures','city', 'likes', 'favorites','post_images')