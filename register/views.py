from django.core import mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import RegisterForm

corpo_email = 'Teste'

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid(): 
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso! Por favor, faça o Login para poder utilizar o sistema.')
            body = render_to_string('register/corpo_email_inscricao.txt', 
                                    form.cleaned_data)
            mail.send_email('Confirmação de inscrição',
                            body,
                            'contato@jurisfai.com.br',
                            ['contato@jurisfai.com.br', 'victorsantos.py@gmail.com', form.cleaned_data['email']])
        
            return redirect('register')
        else:
            return(render(request, 'register/register.html',
                            {'form': form}))
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

