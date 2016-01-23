# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 22:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=100, verbose_name=b'Unidade de Neg\xc3\xb3cios')),
            ],
            options={
                'verbose_name': 'Unidade de Neg\xf3cios',
                'verbose_name_plural': 'Unidades de Neg\xf3cio',
            },
        ),
        migrations.CreateModel(
            name='User_BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_unit', models.ForeignKey(blank=b'true', null=b'true', on_delete=django.db.models.deletion.CASCADE, to='business_unit.BusinessUnit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_business_unit', to=settings.AUTH_USER_MODEL, verbose_name=b'Usu\xc3\xa1rio')),
            ],
            options={
                'verbose_name': 'Unidade de Neg\xf3cio do Usu\xe1rio',
                'verbose_name_plural': 'Unidades de Neg\xf3cio do Usu\xe1rio',
            },
        ),
    ]