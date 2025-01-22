# Generated by Django 3.2.15 on 2025-01-10 11:41

import Formulario.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Formulario', '0006_ini_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='bnup_ingreso',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('estado', models.TextField(blank=True, default='en espera')),
                ('calle', models.TextField(blank=True, null=True)),
                ('ref', models.TextField(blank=True, null=True)),
                ('mat', models.TextField(blank=True, null=True)),
                ('n_de_ingreso', models.TextField(blank=True, null=True)),
                ('codigo', models.BigIntegerField(blank=True, null=True)),
                ('unidad_técnica', models.CharField(blank=True, choices=[('Direcciones de Obras Municipales', 'DOM'), ('Asesoría Urbana', 'AU'), ('', '')], default='', max_length=100)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('archivo_adjunto', models.FileField(blank=True, null=True, upload_to=Formulario.models.content_file_bnup_adjunto)),
                ('constituye', models.CharField(max_length=100)),
                ('otro_constituye', models.TextField(blank=True, null=True)),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
