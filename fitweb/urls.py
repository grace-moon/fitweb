from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('home',views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('email', views.email, name='email'),
    path('post/<int:pk>/', views.detail, name='detail'),

    path('stretching_list', views.stretching_list, name='stretching_list'),
    path('weight_training_list', views.weight_training_list, name='weight_training_list'),


    path('stretching_list_pain_fullbody', views.stretching_list_pain_fullbody, name='stretching_list_pain_fullbody'),
    path('stretching_list_pain_neck', views.stretching_list_pain_neck, name='stretching_list_pain_neck'),
    path('stretching_list_pain_shoulder', views.stretching_list_pain_shoulder, name='stretching_list_pain_shoulder'),
    path('stretching_list_pain_waist', views.stretching_list_pain_waist, name='stretching_list_pain_waist'),
    path('stretching_list_pain_pelvis', views.stretching_list_pain_pelvis, name='stretching_list_pain_pelvis'),
    path('stretching_list_pain_knee', views.stretching_list_pain_knee, name='stretching_list_pain_knee'),
    path('stretching_list_pain_wrist', views.stretching_list_pain_wrist, name='stretching_list_pain_wrist'),
    path('stretching_list_pain_ankle', views.stretching_list_pain_ankle, name='stretching_list_pain_ankle'),



    path('stretching_list_spare_time_fullbody', views.stretching_list_spare_time_fullbody, name='stretching_list_spare_time_fullbody'),
    path('stretching_list_spare_time_top', views.stretching_list_spare_time_top, name='stretching_list_spare_time_top'),
    path('stretching_list_spare_time_bottom', views.stretching_list_spare_time_bottom, name='stretching_list_spare_time_bottom'),

    path('stretching_list_after_wake_up_short', views.stretching_list_after_wake_up_short, name='stretching_list_after_wake_up_short'),
    path('stretching_list_after_wake_up_medium', views.stretching_list_after_wake_up_medium, name='stretching_list_after_wake_up_medium'),
    path('stretching_list_after_wake_up_long', views.stretching_list_after_wake_up_long, name='stretching_list_after_wake_up_long'),

    path('stretching_list_before_bed_short', views.stretching_list_before_bed_short, name='stretching_list_before_bed_short'),
    path('stretching_list_before_bed_medium', views.stretching_list_before_bed_medium, name='stretching_list_before_bed_medium'),
    path('stretching_list_before_bed_long', views.stretching_list_before_bed_long, name='stretching_list_before_bed_long'),

    path('stretching_list_before_exercise_short', views.stretching_list_before_exercise_short, name='stretching_list_before_exercise_short'),
    path('stretching_list_before_exercise_medium', views.stretching_list_before_exercise_medium, name='stretching_list_before_exercise_medium'),
    path('stretching_list_before_exercise_long', views.stretching_list_before_exercise_long, name='stretching_list_before_exercise_long'),

    path('stretching_list_after_exercise_short', views.stretching_list_after_exercise_short,
         name='stretching_list_after_exercise_short'),
    path('stretching_list_after_exercise_medium', views.stretching_list_after_exercise_medium,
         name='stretching_list_after_exercise_medium'),
    path('stretching_list_after_exercise_long', views.stretching_list_after_exercise_long,
         name='stretching_list_after_exercise_long'),

    path('weight_training_list_beginner_level_2parts', views.weight_training_list_beginner_level_2parts,
         name='weight_training_list_beginner_level_2parts'),
    path('weight_training_list_beginner_level_3parts', views.weight_training_list_beginner_level_3parts,
         name='weight_training_list_beginner_level_3parts'),


    path('weight_training_list_intermediate_level_2parts', views.weight_training_list_intermediate_level_2parts,
         name='weight_training_list_intermediate_level_2parts'),
    path('weight_training_list_intermediate_level_3parts', views.weight_training_list_intermediate_level_3parts,
         name='weight_training_list_intermediate_level_3parts'),
    path('weight_training_list_intermediate_level_4parts', views.weight_training_list_intermediate_level_4parts,
         name='weight_training_list_intermediate_level_4parts'),
    path('weight_training_list_intermediate_level_5parts', views.weight_training_list_intermediate_level_5parts,
         name='weight_training_list_intermediate_level_5parts'),


    path('weight_training_list_advanced_level_3parts', views.weight_training_list_advanced_level_3parts,
         name='weight_training_list_advanced_level_3parts'),
    path('weight_training_list_advanced_level_4parts', views.weight_training_list_advanced_level_4parts,
         name='weight_training_list_advanced_level_4parts'),
    path('weight_training_list_advanced_level_5parts', views.weight_training_list_advanced_level_5parts,
         name='weight_training_list_advanced_level_5parts'),

    path('hiit_list', views.hiit_list, name='hiit_list'),
    path('hiit_list_low_level', views.hiit_list_low_level, name='hiit_list_low_level'),
    path('hiit_list_high_level', views.hiit_list_high_level, name='hiit_list_high_level'),

    path('recommend', views.recommend, name='recommend'),

]
