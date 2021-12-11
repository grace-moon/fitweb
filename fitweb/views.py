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



def email(request):
    return render(request, 'fitweb/email.html')

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'fitweb/detail.html', {'post': post})


def stretching_list(request):
    posts = Post.objects.filter(Header_first__contains='stretching')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list.html', {'posts': posts})

def weight_training_list(request):
    posts = Post.objects.filter(Header_first__contains='weight training')
    posts = posts.order_by("title")
    return render(request, 'fitweb/weight_training_list.html', {'posts': posts})

def stretching_list_pain_fullbody(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='full body')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_fullbody.html', {'posts': posts})

def stretching_list_pain_neck(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='neck')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_neck.html', {'posts': posts})

def stretching_list_pain_shoulder(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='shoulder')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_shoulder.html', {'posts': posts})


def stretching_list_pain_waist(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='waist')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_waist.html', {'posts': posts})


def stretching_list_pain_pelvis(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='pelvis')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_pelvis.html', {'posts': posts})


def stretching_list_pain_knee(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='knee')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_knee.html', {'posts': posts})


def stretching_list_pain_wrist(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='wrist')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_wrist.html', {'posts': posts})


def stretching_list_pain_ankle(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='pain relief', Header_third__contains='ankle')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_pain_ankle.html', {'posts': posts})



def stretching_list_spare_time_fullbody(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='spare time', Header_third__contains='full body')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_spare_time_fullbody.html', {'posts': posts})

def stretching_list_spare_time_top(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='spare time', Header_third__contains='top')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_spare_time_top.html', {'posts': posts})

def stretching_list_spare_time_bottom(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='spare time', Header_third__contains='bottom')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_spare_time_bottom.html', {'posts': posts})



def stretching_list_after_wake_up_short(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after wake up', Header_third__contains='short')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_after_wake_up_short.html', {'posts': posts})

def stretching_list_after_wake_up_medium(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after waKe up', Header_third__contains='medium')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_after_wake_up_medium.html', {'posts': posts})

def stretching_list_after_wake_up_long(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after waKe up', Header_third__contains='long')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_after_wake_up_long.html', {'posts': posts})



def stretching_list_before_bed_short(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='before bed', Header_third__contains='short')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_before_bed_short.html', {'posts': posts})

def stretching_list_before_bed_medium(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='before bed', Header_third__contains='medium')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_before_bed_medium.html', {'posts': posts})

def stretching_list_before_bed_long(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='before bed', Header_third__contains='long')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_before_bed_long.html', {'posts': posts})



def stretching_list_before_exercise_short(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='before exercise', Header_third__contains='short')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_before_exercise_short.html', {'posts': posts})

def stretching_list_before_exercise_medium(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='before exercise', Header_third__contains='medium')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_before_exercise_medium.html', {'posts': posts})

def stretching_list_before_exercise_long(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='before exercise', Header_third__contains='long')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_before_exercise_long.html', {'posts': posts})




def stretching_list_after_exercise_short(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after exercise', Header_third__contains='short')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_after_exercise_short.html', {'posts': posts})

def stretching_list_after_exercise_medium(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after exercise', Header_third__contains='medium')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_after_exercise_medium.html', {'posts': posts})

def stretching_list_after_exercise_long(request):
    posts = Post.objects.filter(Header_first__contains='stretching', Header_second__contains='after exercise', Header_third__contains='long')
    posts = posts.order_by("title")
    return render(request, 'fitweb/stretching_list_after_exercise_long.html', {'posts': posts})







def weight_training_list_beginner_level_2parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='beginner', Header_third__contains='part2')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_beginner_level_2parts.html', {'posts': posts})

def weight_training_list_beginner_level_3parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='beginner', Header_third__contains='part3')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_beginner_level_3parts.html', {'posts': posts})




def weight_training_list_intermediate_level_2parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='intermediate', Header_third__contains='part2')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_intermediate_level_2parts.html', {'posts': posts})

def weight_training_list_intermediate_level_3parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='intermediate', Header_third__contains='part3')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_intermediate_level_3parts.html', {'posts': posts})

def weight_training_list_intermediate_level_4parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='intermediate', Header_third__contains='part4')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_intermediate_level_4parts.html', {'posts': posts})

def weight_training_list_intermediate_level_5parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='intermediate', Header_third__contains='part5')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_intermediate_level_5parts.html', {'posts': posts})




def weight_training_list_advanced_level_3parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='advanced', Header_third__contains='part3')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_advanced_level_3parts.html', {'posts': posts})

def weight_training_list_advanced_level_4parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='advanced', Header_third__contains='part4')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_advanced_level_4parts.html', {'posts': posts})

def weight_training_list_advanced_level_5parts(request):
    posts = Post.objects.filter(Header_first__contains='weight training', Header_second__contains='advanced', Header_third__contains='part5')
    posts = posts.order_by("title")
    posts = posts.order_by("Header_four")
    return render(request, 'fitweb/weight_training_list_advanced_level_5parts.html', {'posts': posts})







def hiit_list(request):
    posts = Post.objects.filter(Header_first__contains='hiit')
    posts = posts.order_by("title")
    return render(request, 'fitweb/hiit_list.html', {'posts': posts})

def hiit_list_low_level(request):
    posts = Post.objects.filter(Header_first__contains='hiit', Header_second__contains='low')
    posts = posts.order_by("title")
    return render(request, 'fitweb/hiit_list_low_level.html', {'posts': posts})

def hiit_list_high_level(request):
    posts = Post.objects.filter(Header_first__contains='hiit', Header_second__contains='high')
    posts = posts.order_by("title")
    return render(request, 'fitweb/hiit_list_high_level.html', {'posts': posts})



def recommend(request):
    posts = Post.objects.all()
    posts = posts.order_by("title")
    return render(request, "fitweb/recommend.html", {'posts':posts})

