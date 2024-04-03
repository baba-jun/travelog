from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import DiaryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import diary
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(generic.TemplateView):
    template_name = "index.html"

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = diary
    template_name = "diary_create.html"
    form_class = DiaryCreateForm
    success_url = reverse_lazy("travelog_app:index")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        messages.success(self.request, '投稿完了')
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, '投稿失敗')
        return super().form_invalid(form)