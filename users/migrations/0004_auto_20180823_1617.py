# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-23 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_entradaestoque'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EntradaEstoque',
            new_name='EntradaChipEstoque',
        ),
    ]