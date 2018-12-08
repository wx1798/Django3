# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-29 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180728_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('province', models.CharField(max_length=32)),
                ('dept', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
