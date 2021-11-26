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




def stretching_list(request):
    posts = Post.objects.filter(Header_first__contains='stretching')
    return render(request, 'fitweb/stretching_list.html', {'posts': posts})

def weight_training_list(request):
    posts = Post.objects.filter(Header_first__contains='weight training')
    return render(request, 'fitweb/weight_training_list.html', {'posts': posts})

def stretching_list_pain_fullbody(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='full body')
    return render(request, 'fitweb/stretching_list_pain_fullbody.html', {'posts': posts})

def stretching_list_pain_neck(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='neck')
    return render(request, 'fitweb/stretching_list_pain_neck.html', {'posts': posts})

def stretching_list_pain_shoulder(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='shoulder')
    return render(request, 'fitweb/stretching_list_pain_shoulder.html', {'posts': posts})


def stretching_list_pain_waist(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='waist')
    return render(request, 'fitweb/stretching_list_pain_waist.html', {'posts': posts})


def stretching_list_pain_pelvis(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='pelvis')
    return render(request, 'fitweb/stretching_list_pain_pelvis.html', {'posts': posts})


def stretching_list_pain_knee(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='knee')
    return render(request, 'fitweb/stretching_list_pain_knee.html', {'posts': posts})


def stretching_list_pain_wrist(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='wrist')
    return render(request, 'fitweb/stretching_list_pain_wrist.html', {'posts': posts})


def stretching_list_pain_ankle(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='ankle')
    return render(request, 'fitweb/stretching_list_pain_ankle.html', {'posts': posts})



def stretching_list_spare_time_fullbody(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='spare time', Header_third__contains='full body')
    return render(request, 'fitweb/stretching_list_spare_time_fullbody.html', {'posts': posts})

def stretching_list_spare_time_top(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='spare time', Header_third__contains='top')
    return render(request, 'fitweb/stretching_list_spare_time_top.html', {'posts': posts})

def stretching_list_spare_time_bottom(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='spare time', Header_third__contains='bottom')
    return render(request, 'fitweb/stretching_list_spare_time_bottom.html', {'posts': posts})



def stretching_list_after_wake_up_short(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after wake up', Header_third__contains='short')
    return render(request, 'fitweb/stretching_list_after_wake_up_short.html', {'posts': posts})

def stretching_list_after_wake_up_medium(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after waKe up', Header_third__contains='medium')
    return render(request, 'fitweb/stretching_list_after_wake_up_medium.html', {'posts': posts})

def stretching_list_after_wake_up_long(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after waKe up', Header_third__contains='long')
    return render(request, 'fitweb/stretching_list_after_wake_up_long.html', {'posts': posts})




