# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm

from pathlib import Path
import os

from django.contrib.staticfiles import finders

# Build paths inside the project like this: BASE_DIR / 'subdir'.

User = get_user_model()

def register(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    print('Base Directory : ', os.path.join(BASE_DIR, 'static/'))

    result = finders.find('register/register.css')
    print(result)
    print('S : ', finders.searched_locations)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            form.save()
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
            except:
                user = None
            
            if user != None:
                return redirect('/login')
            else:
                request.session['register_error'] = 1
    else:
        form = RegisterForm()
    
    return render(request, 'register/register.html', {'form': form})