from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def authorization(request):
    error = ''
    if request.method == 'POST':
        
        form = UsersForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = hash_password(form.cleaned_data['password'])
            new_user.save()
        else:
            error = 'Форма неверна.'
    form = UsersForm()
    
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'users/authorization.html', data)


