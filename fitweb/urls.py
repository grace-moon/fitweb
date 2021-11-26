from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('home',views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('how_to_use', views.how_to_use, name='how_to_use'),
    path('email', views.email, name='email'),
    path('list', views.list, name='list'),
    path('post/<int:pk>/', views.detail, name='detail'),

    path('stretching_list', views.stretching_list, name='stretching_list'),

    path('stretching_list_pain_fullbody', views.stretching_list_pain_fullbody, name='stretching_list_pain_fullbody'),
    path('stretching_list_pain_neck', views.stretching_list_pain_neck, name='stretching_list_pain_neck'),
    path('stretching_list_pain_shoulder', views.stretching_list_pain_shoulder, name='stretching_list_pain_shoulder'),
    path('stretching_list_pain_waist', views.stretching_list_pain_waist, name='stretching_list_pain_waist'),
    path('stretching_list_pain_pelvis', views.stretching_list_pain_pelvis, name='stretching_list_pain_pelvis'),
    path('stretching_list_pain_knee', views.stretching_list_pain_knee, name='stretching_list_pain_knee'),
    path('stretching_list_pain_wrist', views.stretching_list_pain_wrist, name='stretching_list_pain_wrist'),
    path('stretching_list_pain_ankle', views.stretching_list_pain_ankle, name='stretching_list_pain_ankle'),



    path('stretching_spare_fullbody', views.stretching_spare_fullbody, name='stretching_spare_fullbody'),
    path('stretching_spare_top', views.stretching_spare_top, name='stretching_spare_top'),
    path('stretching_spare_bottom', views.stretching_spare_bottom, name='stretching_spare_bottom'),

]
