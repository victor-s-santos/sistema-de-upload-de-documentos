from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver

class Documentos(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, default='Arquivo')
    documento = models.FileField()
    data = models.DateField(auto_now_add=True)
    trabalhado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.nome