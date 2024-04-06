from django import forms
from .models import diary, prefectures, cities

class CustomPrefecturesModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.prefecture_name

class CustomCitiesModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.city_name

class DiaryCreateForm(forms.ModelForm):
    prefectures = CustomPrefecturesModelChoiceField(queryset=prefectures.objects.all())
    city = CustomCitiesModelChoiceField(queryset=cities.objects.all())
    class Meta:
        model = diary
        fields = ('title', 'comment', 'country', 'prefectures','city','post_image1','post_image2','post_image3','post_image4')
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'どこに行った？','class': 'form-control'}),
            'comment' : forms.Textarea(attrs={'placeholder': 'どうだった？','class': 'form-control'}),
            'country' : forms.TextInput(attrs={'placeholder': '国を入力'}),
            'city': forms.TextInput(attrs={'placeholder': '市町村区を入力','class': 'form-control'}),
        }