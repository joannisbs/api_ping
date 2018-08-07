# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# USUARIOS
class User(models.Model):
    user_nome = models.CharField(max_length=45)
    user_pass = models.CharField(max_length=32)
    user_tipe = models.CharField(max_length=1)
    user_ativo = models.CharField(max_length=1, default='s')   

class Sessionini(models.Model):
    user_ids   = models.IntegerField(default=0)
    token     = models.CharField(max_length=64)
    user_tipe = models.CharField(max_length=1)   
    ativo     = models.BooleanField(default=False)
    horaini   = models.IntegerField(default=0)
    
class HistoryUser(models.Model):
    user_ids = models.IntegerField(default=0)
    hora     = models.CharField(max_length=17)
    event    = models.CharField(max_length=100)

#CHIP
class Chip(models.Model):
    chip_ip       = models.CharField(max_length=45)
    chip_num      = models.CharField(max_length=8)
    chip_oper     = models.CharField(max_length=15)
    chip_data     = models.CharField(max_length=17)
    chip_ativo    = models.CharField(max_length=1, default='s')
    chip_where    = models.CharField(max_length=1, default='e')# e=estoque s=saida m=modulo
    chip_whedes   = models.IntegerField(default=0)# quem qual

class ChipSaidas(models.Model):
    chip_id       = models.IntegerField(default=0)
    chip_data     = models.CharField(max_length=17)
    saida_autorz  = models.CharField(max_length=45)
    saida_para    = models.CharField(max_length=45)

class HistoryChip(models.Model):
    chip_id  = models.IntegerField(default=0)
    hora     = models.CharField(max_length=17)
    event    = models.CharField(max_length=100)