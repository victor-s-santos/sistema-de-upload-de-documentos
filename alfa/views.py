from django.shortcuts import render, redirect, get_object_or_404
#from django.core import mail
from django.contrib.auth.decorators import login_required
from .forms import DocumentosForm
from .models import Documentos
from django.forms import modelformset_factory

corpo_email = 'Aviso automático, novo documento enviado. Um usuário acabou de enviar um documento para análise.'

@login_required(login_url='/login')
def upload_documento(request):
	DocumentosFormset = modelformset_factory(Documentos, fields=('nome','documento'), extra=5)
	if request.method == 'POST':
		form = DocumentosForm(request.POST, request.FILES)
		formset = DocumentosFormset(request.POST or None, request.FILES or None)
		if form.is_valid() and formset.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()

			for f in formset:
				try:
					documento = Documentos(user=post.user,nome = f.cleaned_data['nome'], documento=f.cleaned_data['documento'])
					documento2 = documento.save()
				except:
					break
			return redirect('documentos_lista')
	else:
		form = DocumentosForm()
		formset = DocumentosFormset(queryset = Documentos.objects.none())
	return render(request, 'upload_documento.html', {
		'form': form,
		'formset': formset
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
