# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from django.contrib import messages

def register(request):

    User = get_user_model()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            form.save()
            try:
                messages.add_message(request, messages.SUCCESS, 'Kullanıcı oluşturuldu giriş yapabilirsiniz.')
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