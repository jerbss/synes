# Generated by Django 5.1.3 on 2025-01-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_synes', '0021_customuser_levar_bola'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/', verbose_name='Foto de Perfil'),
        ),
    ]
