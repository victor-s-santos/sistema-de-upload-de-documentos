# Generated by Django 2.1 on 2020-08-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0002_auto_20200810_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='documento',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='nome',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
