# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsistas_praec', '0004_siape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_preenchimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_preenchimento_termino',
            field=models.DateField(),
        ),
    ]