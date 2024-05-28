from django.shortcuts import render
from likes.models import Like
from django.http import JsonResponse
from likes.models import Like

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def teachers(request):
    return render(request, 'main/teachers.html')

def aboutUs(request):
    return render(request, 'main/aboutUs.html')



def get_likes_count(request):
    # form_data_id = request.GET.get('form_data_id', 'default_value') 
    sonya_likes_count = Like.objects.filter(form_data_id='sonya').count()
    lesha_likes_count = Like.objects.filter(form_data_id='lesha').count()
    nastya_likes_count = Like.objects.filter(form_data_id='nastya').count()
    chmo_likes_count = Like.objects.filter(form_data_id='chmo').count()

    data = {
        'sonya_likes_count': sonya_likes_count,
        'lesha_likes_count': lesha_likes_count,
        'nastya_likes_count': nastya_likes_count,
        'chmo_likes_count': chmo_likes_count,
    }

    return JsonResponse(data)

