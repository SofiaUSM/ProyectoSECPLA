# Generated by Django 3.2.15 on 2024-12-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0004_rename_nombre_proyecto_iniciativa_nombre_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='iniciativa',
            name='detalle_terreno',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='detalle_visita',
            field=models.TextField(blank=True, default=''),
        ),
    ]
