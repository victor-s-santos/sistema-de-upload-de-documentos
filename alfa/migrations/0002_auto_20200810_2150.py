# Generated by Django 2.1 on 2020-08-10 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentos',
            old_name='formatado',
            new_name='trabalhado',
        ),
    ]
