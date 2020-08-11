from django.core import mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm

corpo_email = 'Teste'

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso! Por favor, faça o Login para poder utilizar o sistema.')
            mail.send_email('Confirmação de inscrição',
                            message,
                            'contato@jurisfai.com.br',
                            ['contato@jurisfai.com.br', 'victorsantos.py@gmail.com'])
        return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

message = 
"""
Olá, o seu usuário já se encontra disponível!

Agradecemos a sua inscrição, utilizando o nome de usuário cadastrado já é possível submeter documentos à análise.
Mais uma vez, muito obrigado pela confiança em nosso produto.

Nome de usuário:
Email:

Atenciosamente,
Equipe JurisfAI
"""