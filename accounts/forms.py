from allauth.account.forms import SignupForm
from django import forms
class CustomSignupForm(SignupForm): #SignupFormを継承する
    nick_name = forms.CharField(max_length=30, label='ニックネーム')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'ユーザーID'
        self.fields['username'].widget.attrs['placeholder'] = '英数字, "_"のみ入力可能'
        self.fields['nick_name'].widget.attrs['placeholder'] = '日本語での入力も可能'
    
    def signup(self, request, user):
        user.nick_name = self.cleaned_data['nick_name']
        user.save()
        return user