# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_nome = models.CharField(max_length=45)
    user_pass = models.CharField(max_length=32)
    user_tipe = models.CharField(max_length=1)   

class Sessionini(models.Model):
    user_ids   = models.IntegerField(default=0)
    token     = models.CharField(max_length=64)
    user_tipe = models.CharField(max_length=1)   
    ativo     = models.BooleanField(default=False)
    horaini   = models.IntegerField(default=0)
    


