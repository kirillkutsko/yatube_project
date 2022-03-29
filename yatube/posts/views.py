from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f'Главная страница проекта сообщество')

def group_posts(request, slug):
    return HttpResponse(f'Страницы, на которых будут посты, отфильтрованные по группам {slug}')