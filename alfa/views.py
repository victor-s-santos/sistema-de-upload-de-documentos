from django.shortcuts import render, redirect, get_object_or_404
#from django.core import mail
from django.contrib.auth.decorators import login_required
from .forms import DocumentosForm
from .models import Documentos

corpo_email = 'Aviso automático, novo documento enviado. Um usuário acabou de enviar um documento para análise.'

@login_required(login_url='/login')
def upload_documento(request):
	if request.method == 'POST':
		form = DocumentosForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('documentos_lista')
	else:
		form = DocumentosForm()
	return render(request, 'upload_documento.html', {
		'form': form
	})

@login_required(login_url='/login')
def documentos_lista(request):
	docs = Documentos.objects.filter(user=request.user)
	return render(request, 'lista_documentos.html',{
		'docs': docs
	})

def documento_detalhe(request, pk):
	doc = get_object_or_404(Documentos, pk=pk)
	return render(request, 'detalhes.html', {'doc': doc})
