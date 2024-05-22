from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import DiaryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import diary, prefectures, cities, areas, likes
from django.urls import reverse_lazy
from django.contrib import messages
import csv
from io import TextIOWrapper
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import os
import PIL.Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile




class IndexView(generic.ListView):
    template_name = "index.html"
    model = diary

class HomeView(generic.ListView):
    template_name = "home.html"
    model = diary

    def get_context_data(self, **kwargs,): #ユーザが既にイイねしているかどうかの判断
        context = super().get_context_data(**kwargs)

        user = self.request.user

        liked_diaries_ids = likes.objects.filter(user_id = user.id).values_list('diary_id', flat=True)

        liked_diaries_ids = {
            'liked_diaries_ids' : liked_diaries_ids,
        }
        context.update(liked_diaries_ids)
        print(liked_diaries_ids)

        return context


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = diary
    template_name = "diary_create.html"
    form_class = DiaryCreateForm
    success_url = reverse_lazy("travelog_app:Home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        save_path = str("media/"+self.request.FILES['post_image1'].name)
        up_data = self.request.FILES['post_image1']
        with open(save_path, 'wb+') as i:
            for chunk in up_data.chunks():
                i.write(chunk)
        with PIL.Image.open(save_path) as image:
            os.remove(save_path)
            
            resized_height = 640 / int(image.size[0]) * image.size[1]
            resized_image = image.resize((640, int(resized_height)))
            if resized_height > 480:
                resized_width = 480 / int(image.size[1]) * image.size[0]
                resized_image = resized_image.resize((int(resized_width), 480))

            image_io = io.BytesIO()
            resized_image.save(image_io, format="JPEG")
            image_file = InMemoryUploadedFile(image_io, field_name=None, name=save_path,
                                              content_type="image/jpeg", size=image_io.getbuffer().nbytes,
                                              charset=None)
        
        post = form.save(commit=False)
        post.user_id = self.request.user
        post.post_image1 = image_file
        post.save()
        messages.success(self.request, '投稿完了')
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, '投稿失敗')
        return super().form_invalid(form)

class ProfileView(generic.ListView):
    template_name = "profile.html"
    model = diary

    def get_context_data(self, **kwargs,): #ユーザが既にイイねしているかどうかの判断
        context = super().get_context_data(**kwargs)

        user = self.request.user

        liked_diaries_ids = likes.objects.filter(user_id = user.id).values_list('diary_id', flat=True)

        liked_diaries_ids = {
            'liked_diaries_ids' : liked_diaries_ids,
        }
        context.update(liked_diaries_ids)
        print(liked_diaries_ids)

        return context

def like_for_diary(request):
    diary_id = request.POST.get('diary_id')
    context = {
        'user': request.user.id,
    }
    diary_ojb = get_object_or_404(diary, id=diary_id)
    like = likes.objects.filter(diary_id=diary_ojb, user_id=request.user.id)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(diary_id=diary_ojb, user_id=request.user)
        context['method'] = 'create'

    context['like_for_diary_count'] = diary_ojb.likes_set.count()


    return JsonResponse(context)



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
            print(line[2])
            city.save()

    elif 'csv_area' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv_area'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        prefecture = prefectures()
        for line in csv_file:
            area = areas()
            area.prefecture_name = prefectures.objects.get(prefecture_name=line[0])
            area.area_name = line[1]
            print(line[1])
            area.save()


    return render(request, 'csv_upload.html')

def get_area_dropdown(request):
    prefectures_dropdown_text = request.GET.get('prefectures_text')

    area_dropdown_choices = areas.objects.filter(prefecture_name = prefectures_dropdown_text).values("area_name","area_name")

    area_dropdown_choices_list = [{'area_name': '選択してください', 'area_name': ''}]
    area_dropdown_choices_list.extend(list(area_dropdown_choices))

    return JsonResponse({'area_dropdown_choices': area_dropdown_choices_list})
