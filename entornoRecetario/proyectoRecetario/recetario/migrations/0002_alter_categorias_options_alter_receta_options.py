# Generated by Django 4.1.5 on 2023-01-24 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'ordering': ['-created'], 'verbose_name': 'categoria', 'verbose_name_plural': 'categoria'},
        ),
        migrations.AlterModelOptions(
            name='receta',
            options={'ordering': ['-created'], 'verbose_name': 'receta', 'verbose_name_plural': 'recetas'},
        ),
    ]