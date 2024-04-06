from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import DiaryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import diary, prefectures, cities
from django.urls import reverse_lazy
from django.contrib import messages
import csv
from io import TextIOWrapper, StringIO
from django.http import JsonResponse


class IndexView(generic.TemplateView):
    template_name = "index.html"

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = diary
    template_name = "diary_create.html"
    form_class = DiaryCreateForm
    success_url = reverse_lazy("travelog_app:index")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        post = form.save(commit=False)
        post.user_id = self.request.user
        post.save()
        messages.success(self.request, '投稿完了')
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, '投稿失敗')
        return super().form_invalid(form)

def upload_csv_data(request):
    if 'csv_prefecture' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv_prefecture'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        prefecture = prefectures()
        for line in csv_file:
            prefecture.prefecture_id = line[0]
            prefecture.prefecture_name=line[1]
            prefecture.save()

    elif 'csv_city' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv_city'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        city = cities()
        prefecture = prefectures()
        for line in csv_file:
            city.city_id = line[0]
            city.city_name = line[1]
            city.prefecture_id = prefectures.objects.get(prefecture_id = line[2])
            city.save()


    return render(request, 'csv_upload.html')

def get_city_dropdown(request):
    prefectures_dropdown_value = request.GET.get('id_prefectures_value')

    city_dropdown_choices = cities.objects.filter(prefecture_id = prefectures_dropdown_value).values("city_name")
    
    city_dropdown_choices_list = list(city_dropdown_choices)
    print(city_dropdown_choices_list)
    
    return JsonResponse({'city_dropdown_choices': city_dropdown_choices_list})
