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
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default=b'000', max_length=10, verbose_name=b'C\xc3\xb3digo')),
                ('descricao', models.CharField(default=b'Produto', max_length=100, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('preco_unit', models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name=b'Pre\xc3\xa7o Unit\xc3\xa1rio')),
                ('business_unit', models.ForeignKey(blank=b'true', null=b'true', on_delete=django.db.models.deletion.CASCADE, to='business_unit.BusinessUnit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]