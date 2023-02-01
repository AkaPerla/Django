# Generated by Django 4.1.6 on 2023-02-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre')),
                ('tipo', models.CharField(max_length=255, verbose_name='tipo')),
                ('direccion', models.CharField(max_length=255, verbose_name='direccion')),
                ('telefono', models.CharField(max_length=255, verbose_name='telefono')),
                ('personaContacto', models.CharField(max_length=255, verbose_name='personaContacto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('upadted', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificiacion')),
            ],
        ),
    ]