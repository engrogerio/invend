# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comanda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total_item',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name=b'Total'),
        ),
    ]