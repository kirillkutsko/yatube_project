from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {'text': text,}
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_posts.html'
    text = '"Здесь будет информация о группах проекта Yatube'
    context = {'text': text,}
    return render(request, template, context)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)