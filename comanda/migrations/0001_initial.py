# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('produto', '0001_initial'),
        ('business_unit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(default=b'00000', max_length=5, verbose_name=b'Numero')),
                ('status', models.IntegerField(choices=[(1, b'Aberto'), (2, b'Encerrado'), (3, b'Excluido')], default=1, verbose_name=b'Status da Comanda')),
                ('metodo_pagto', models.IntegerField(choices=[(1, b'Dinheiro'), (2, b'Cart\xc3\xa3o d\xc3\xa9bito'), (3, b'Cart\xc3\xa3o cr\xc3\xa9dito'), (4, b'Cheque'), (5, b'Carteira')], default=1, verbose_name=b'Metodo de Pagamento')),
                ('business_unit', models.ForeignKey(blank=b'true', null=b'true', on_delete=django.db.models.deletion.CASCADE, to='business_unit.BusinessUnit')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name=b'Quantidade')),
                ('preco_unit', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name=b'Pre\xc3\xa7o Unit\xc3\xa1rio (R$)')),
                ('total_item', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name=b'Total (R$)')),
                ('comanda', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comanda.Comanda')),
                ('produto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
        ),
    ]
