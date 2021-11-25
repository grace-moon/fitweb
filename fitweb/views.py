# video/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post


def main(request):
    return render(request, 'fitweb/main.html')

def home(request):
    return render(request, 'fitweb/home.html')

#about_us 소개
def about_us(request):
    return render(request, 'fitweb/about_us.html')

def how_to_use(request):
    return render(request, 'fitweb/how_to_use.html')

def email(request):
    return render(request, 'fitweb/email.html')

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'fitweb/detail.html', {'post': post})

def list(request):
    posts = Post.objects.all()
    return render(request, 'fitweb/list.html', {'posts': posts})

def stretching_home(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭')
    return render(request, 'fitweb/stretching_home.html', {'posts': posts})

def stretching_secondhome(request):
    posts =Post.objects.filter(Header_second__contains='통증')
    return render(request, 'fitweb/stretching_secondhome.html', {'posts': posts})