# Generated by Django 5.0.3 on 2024-04-18 18:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreProyecto', models.CharField(max_length=200)),
                ('NumEspecies', models.PositiveIntegerField()),
                ('NumEstaciones', models.PositiveIntegerField()),
                ('EstudioInicio', models.DateTimeField(null=True)),
                ('EstudioFin', models.DateTimeField(null=True)),
                ('ConjuntoDatos', models.BinaryField(null=True)),
                ('CamarasInfo', models.BinaryField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]