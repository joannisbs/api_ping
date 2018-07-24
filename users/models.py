# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

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
    
class History(models.Model):
    user_ids = models.IntegerField(default=0)
    hora     = models.CharField(max_length=17)
    event    = models.CharField(max_length=100)

class Chip(models.Model):
    chip_ip       = models.CharField(max_length=45)
    chip_num      = models.CharField(max_length=8)
    chip_oper     = models.CharField(max_length=15)
    chip_data     = models.CharField(max_length=17)