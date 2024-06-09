from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import get_user_model
from django.core.exceptions import PermissionDenied
from django.forms import ValidationError
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):

    def clean_username(self, username):
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            raise ValidationError("このユーザー名は既に使用されています。")
        return username

    def get_login_form_class(self):
        from .forms import CustomLoginForm
        return CustomLoginForm