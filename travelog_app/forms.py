from django import forms
from .models import diary, prefectures, areas

class CustomPrefecturesModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.prefecture_name

class CustomAreasModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.area_name

class DiaryCreateForm(forms.ModelForm):
    prefectures = CustomPrefecturesModelChoiceField(queryset=prefectures.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), required = False)
    areas = CustomAreasModelChoiceField(queryset=areas.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), required = False)
    country = forms.ChoiceField(
        choices=(
            ('日本', '日本'),
            ),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required = False,
    )
    class Meta:
        model = diary
        fields = ('title', 'comment', 'country', 'prefectures','city','post_image1','post_image2','post_image3','post_image4')
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'タイトルを入力','class': 'form-control'}),
            'comment' : forms.Textarea(attrs={'placeholder': 'コメントを入力','class': 'form-control'}),
        }