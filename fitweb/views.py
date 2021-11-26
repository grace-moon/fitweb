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



def stretching_pain_category(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증')
    return render(request, 'fitweb/stretching_pain_category.html', {'posts': posts})


def stretching_list(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증')
    return render(request, 'fitweb/stretching_list.html', {'posts': posts})


def stretching_list_pain_fullbody(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='전신')
    return render(request, 'fitweb/stretching_list_pain_fullbody.html', {'posts': posts})

def stretching_list_pain_neck(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='목,')
    return render(request, 'fitweb/stretching_list_pain_neck.html', {'posts': posts})

def stretching_list_pain_shoulder(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='어깨')
    return render(request, 'fitweb/stretching_list_pain_shoulder.html', {'posts': posts})


def stretching_list_pain_waist(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='허리')
    return render(request, 'fitweb/stretching_list_pain_waist.html', {'posts': posts})


def stretching_list_pain_pelvis(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='골반')
    return render(request, 'fitweb/stretching_list_pain_pelvis.html', {'posts': posts})


def stretching_list_pain_knee(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='무릎')
    return render(request, 'fitweb/stretching_list_pain_knee.html', {'posts': posts})


def stretching_list_pain_wrist(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='손목')
    return render(request, 'fitweb/stretching_list_pain_wrist.html', {'posts': posts})


def stretching_list_pain_ankle(request):
    posts = Post.objects.filter(Header_first__contains='스트레칭', Header_second__contains='통증', Header_third__contains='발목')
    return render(request, 'fitweb/stretching_list_pain_ankle.html', {'posts': posts})
