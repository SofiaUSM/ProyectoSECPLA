# Generated by Django 3.2.15 on 2025-01-22 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0010_auto_20250110_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bnup_ingreso',
            name='estado',
        ),
    ]
