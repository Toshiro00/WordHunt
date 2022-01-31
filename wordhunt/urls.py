"""wordhunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v_register
from learn import views as v_learn
from user_profile import views as v_user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_user_profile.profile, name='profile'),
    path('register/', v_register.register, name='register'),
    path('translate/', v_learn.translate_page, name='translate_page'),
    path('wordpoolquiz/', v_learn.word_pool_quiz, name='word_pool_quiz'),
    path('wordpool/', v_learn.word_pool, name='word_pool'),
    path('newword/', v_learn.new_word, name='new_word'),
    path('wronganswers/', v_learn.wrong_answers, name='wrong_answers'),
    path('', include('django.contrib.auth.urls')),
]
