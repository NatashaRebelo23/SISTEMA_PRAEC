# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=80)),
                ('cpf', models.CharField(max_length=15)),
                ('curso', models.CharField(max_length=80)),
                ('renda_familiar', models.CharField(max_length=15)),
                ('data_preenchimento', models.DateField(auto_now=True)),
                ('data_preenchimento_termino', models.DateField(auto_now=True)),
            ],
        ),
    ]