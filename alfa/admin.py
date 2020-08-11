from django.contrib import admin
from .models import Documentos


class DocumentosAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_display = ['user', 'nome', 'documento', 'data', 'trabalhado']
    search_fields = ['user', 'nome', 'documento', 'data', 'trabalhado']
    list_filter = ['user', 'nome', 'documento', 'data', 'trabalhado']

admin.site.register(Documentos, DocumentosAdmin)
# Register your models here.
