
from django.shortcuts import render
from .forms import LikeForm
from .models import Like
from django.utils import timezone

def like_view(request):
    error = ''
    if request.method == 'POST':
        form_data_id = request.POST.get('form_data_id')

        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save(commit=False)
            like.user = request.user
            like.form_data_id = form_data_id
            like.timestamp = timezone.now()
            # Проверяем наличие записи с таким же form_data_id и user
            existing_like = Like.objects.filter(form_data_id=form_data_id, user=request.user).first()
            if existing_like:
                existing_like.delete()  # Удаляем существующую запись
            else:
                like.save()
        else:
            error = form.errors
        
    form = LikeForm()
    
    data = {
        'form': form,
        'error': error
    }
    

    return render(request, 'main/teachers.html', data)
