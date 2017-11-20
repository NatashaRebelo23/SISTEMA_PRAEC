# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsistas_praec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolsa_Auxilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('REU', 'REU'), ('ITA', 'ITA'), ('KIT ODONTOLOGICO', 'KIT ODONTOLOGICO'), ('KIT LUPAS MANUAIS', 'KIT LUPAS MANUAIS')], max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Bolsa_Remunerada_400',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('BAE', 'BAE'), ('BIAMA', 'BIAMA'), ('BINCS', 'BINCS'), ('APEC', 'APEC'), ('BIAE', 'BIAE'), ('BIAF', 'BIAF')], max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='periodo',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='bolsa_remunerada_400',
            name='aluno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bolsistas_praec.Aluno'),
        ),
        migrations.AddField(
            model_name='bolsa_auxilio',
            name='aluno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bolsistas_praec.Aluno'),
        ),
    ]
