# Generated by Django 3.2.15 on 2024-12-17 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0002_auto_20241217_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iniciativa',
            old_name='asamblea_analisis',
            new_name='analisis_adjunto',
        ),
    ]
