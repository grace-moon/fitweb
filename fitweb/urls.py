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
    path('stretching_home',views.stretching_home, name='stretching_home'),
    path('stretching_secondhome', views.stretching_secondhome, name='stretching_secondhome'),
]