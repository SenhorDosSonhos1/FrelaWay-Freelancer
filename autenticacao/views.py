from django.shortcuts import render
from django.http import HttpResponse

#Cadastro
from .utils import register_valid_inputs
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User

#Login e Logout
from django.contrib import auth

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        valid_inputs = register_valid_inputs(request, username, password, confirm_password)
        
        user = User.objects.filter(username=username)
        
        if not valid_inputs:  
            return redirect('/auth/cadastro')
        
        elif user.exists():
            messages.add_message(request, constants.ERROR, 'O nome de usúario já está em uso.')
            return redirect('/auth/cadastro')
        
        else:
            try:    
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                
                return redirect('/auth/login')
            except:
                messages.add_message(request, constants.ERROR, 'Erro interno do sistema contate um administrador.')
                return redirect('/auth/cadastro') 

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "GET":
         return render(request, 'login.html')
     
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = auth.authenticate(
        username=username,
        password=password
    )
    
    if user is not None:
        auth.login(request, user)
        return redirect('/jobs/encontrar_jobs')
    
    else:
        messages.add_message(request, constants.ERROR, 'Credenciais inválidas ou o usuário não existe.')
        return redirect('/auth/login')
      
def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
