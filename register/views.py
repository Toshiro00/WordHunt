# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm

User = get_user_model()

def register(request):
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