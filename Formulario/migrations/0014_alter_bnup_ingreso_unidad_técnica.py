# Generated by Django 3.2.15 on 2025-01-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0013_auto_20250122_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnup_ingreso',
            name='unidad_técnica',
            field=models.CharField(blank=True, choices=[('', ''), ('Asesoría Urbana', 'AU'), ('Dirección de Obras Municipales', 'DOM')], default='', max_length=100),
        ),
    ]
