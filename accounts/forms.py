from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from django import forms

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = "Username"
        self.fields['login'].widget.attrs.update({
            'placeholder': 'Username',
        })
        
class CustomSignupForm(SignupForm):
    display_name = forms.CharField(label = "ニックネーム", required=True)
    profile_img = forms.ImageField(label='プロフィール画像')
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.display_name = self.cleaned_data['display_name']
        user.profile_img = self.cleaned_data['profile_img']
        user.save()
        return user
