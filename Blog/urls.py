from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('Blog/', views.blog, name='Blog'),
    path('show_all/', views.show_all, name='show_all'),
    path('about/', views.about, name='about'),
]