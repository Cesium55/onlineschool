from django.urls import path
from .views import like_view

urlpatterns = [
    path('like/', like_view, name='like'),
]