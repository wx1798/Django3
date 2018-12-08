# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-29 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'dept',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('salary', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Dept')),
            ],
            options={
                'db_table': 'people',
            },
        ),
    ]
