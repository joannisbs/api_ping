# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-16 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('chip_ativo', models.CharField(default='s', max_length=1)),
                ('chip_where', models.CharField(default='e', max_length=1)),
                ('chip_whedes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ChipSaidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip_id', models.IntegerField(default=0)),
                ('chip_data', models.CharField(max_length=17)),
                ('saida_autorz', models.CharField(max_length=45)),
                ('saida_para', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_nome', models.CharField(max_length=12)),
                ('empdata_cnpj', models.CharField(max_length=18)),
                ('empdata_email', models.CharField(max_length=60)),
                ('empdata_razao', models.CharField(max_length=90)),
                ('empdata_resp', models.CharField(max_length=45)),
                ('empdata_tel', models.CharField(max_length=14)),
                ('end_bairro', models.CharField(max_length=45)),
                ('end_cep', models.CharField(max_length=45)),
                ('end_cidade', models.CharField(max_length=45)),
                ('end_comp', models.CharField(max_length=45)),
                ('end_num', models.CharField(max_length=45)),
                ('end_ref', models.CharField(max_length=45)),
                ('end_rua', models.CharField(max_length=60)),
                ('end_uf', models.CharField(max_length=2)),
                ('cont_On', models.CharField(max_length=3)),
                ('cont_Tot', models.CharField(max_length=3)),
                ('emp_ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaChipEstoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip_id', models.IntegerField(default=0)),
                ('chip_data', models.CharField(max_length=17)),
                ('entradapor', models.CharField(max_length=45)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryChip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip_id', models.IntegerField(default=0)),
                ('hora', models.CharField(max_length=17)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryEmpresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField(default=0)),
                ('hora', models.CharField(max_length=17)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ids', models.IntegerField(default=0)),
                ('hora', models.CharField(max_length=17)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sessionini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ids', models.IntegerField(default=0)),
                ('token', models.CharField(max_length=64)),
                ('user_tipe', models.CharField(max_length=1)),
                ('ativo', models.BooleanField(default=False)),
                ('horaini', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nome', models.CharField(max_length=45)),
                ('user_pass', models.CharField(max_length=32)),
                ('user_tipe', models.CharField(max_length=1)),
                ('user_ativo', models.CharField(default='s', max_length=1)),
            ],
        ),
    ]
