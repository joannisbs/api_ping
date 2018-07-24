# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip_ip', models.CharField(max_length=45)),
                ('chip_num', models.CharField(max_length=8)),
                ('chip_oper', models.CharField(max_length=15)),
                ('chip_data', models.CharField(max_length=17)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_ativo',
            field=models.CharField(default='s', max_length=1),
        ),
    ]
