# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsistas_praec', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siape', models.CharField(max_length=9)),
            ],
        ),
    ]
