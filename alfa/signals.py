from django.db.models import signals
from django.dispatch import receiver
from .models import Documentos
from django.core import mail

message = 'O documento enviado ao nosso sistema já se encontra trabalhado. Para acessá-lo, por favor retorne ao sistema.'

@receiver(signals.post_save, sender=Documentos)
def documento_enviado(sender, instance, created, **kwargs):
    if instance.trabalhado == True:
        mail.send_mail('Obrigado por utilizar nosso sistema!',
                                message,
                                'victorsantos.py@gmail.com',#remetente
                                ['victorsantos.py@gmail.com', instance.user.email] #destinatário
                                )

    