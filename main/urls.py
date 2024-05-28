
from django.urls import path
from likes import views as lv
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('like', lv.like_view, name='like'),
    path('likes_count/', views.get_likes_count, name='likes_count'),
]