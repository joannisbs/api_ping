# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_session_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='horaini',
            field=models.IntegerField(default=0),
        ),
    ]
