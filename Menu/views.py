from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,update_session_auth_hash, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import *

# Create your views here.

@login_required(login_url='/login/')
def Inicio(request):
    users = User.objects.all()

    data = {
        'users':users,
    }
    return redirect('menu')

def login(request):
    if request.user.is_authenticated:
        return redirect('menu')

    if request.method == 'POST':
        email = request.POST.get('email')
        email = email.lower()
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'Login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')