from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from register import views as v
from alfa import views as alfa_v
from core import views as core_v
from django.urls import path, include

urlpatterns = [
    #-- página inicial --#
    path('', core_v.index, name='index'),
    #-- página de upload --#
    path('upload/', alfa_v.upload_documento, name='upload'),
    #--lista de documentos enviados --#
    path('documentos/', alfa_v.documentos_lista, name='documentos_lista'),
    #--detalhes do documento -- #
    path('documentos/<int:pk>/', alfa_v.documento_detalhe, name='doc_detalhe'),
    
    #-- cadastro --#
    path('register/', v.register, name='register'),
    #--login--#
    path('', include('django.contrib.auth.urls'), name='login'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
