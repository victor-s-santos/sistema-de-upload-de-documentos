from django.contrib import messages
from django.core import mail
from django.shortcuts import render, redirect
from .forms import RegisterForm

corpo_email = 'Aviso automático, um novo usuário cadastrado no sistema.'

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Usuário cadastrado com sucesso! Por favor, faça o Login para poder utilizar o sistema.')
        """mail.send_mail('Novo usuário cadastrado.',
                            corpo_email,
                            'contato@gmail.com',
                            ['victorsantos.py@gmail.com']
                            )"""
        return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})
# Create your views here.
