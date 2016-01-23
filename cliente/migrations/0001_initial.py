# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_unit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=b'Cliente Nome', max_length=60, verbose_name=b'Nome')),
                ('endereco', models.CharField(blank=True, max_length=200, verbose_name=b'Endere\xc3\xa7o')),
                ('telefone', models.CharField(blank=True, max_length=20, verbose_name=b'Telefone')),
                ('celular', models.CharField(blank=True, max_length=20, verbose_name=b'Celular')),
                ('cpf', models.CharField(blank=True, max_length=15, verbose_name=b'CPF')),
                ('business_unit', models.ForeignKey(blank=b'true', null=b'true', on_delete=django.db.models.deletion.CASCADE, to='business_unit.BusinessUnit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
