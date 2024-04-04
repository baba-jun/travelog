from django import forms
from .models import diary
 
class DiaryCreateForm(forms.ModelForm):
    prefectures = forms.ChoiceField(
    choices = (
    ('千葉県','千葉県'),
    ('東京都','東京都'),
    ('神奈川県','神奈川県'),
    ),
    required=True,
    widget=forms.widgets.Select
    )
    class Meta:
        model = diary
        fields = ('title', 'comment', 'country', 'prefectures','city','post_image1','post_image2','post_image3','post_image4')
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'タイトルを入力'}),
            'comment' : forms.Textarea(attrs={'placeholder': 'コメントを入力'}),
            'country' : forms.TextInput(attrs={'placeholder': '国を入力'}),
            'city': forms.TextInput(attrs={'placeholder': '市町村区を入力'}),
        }