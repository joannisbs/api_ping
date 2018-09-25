# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# USUARIOS
class User(models.Model):
    user_nome       = models.CharField      ( max_length = 45 )
    user_pass       = models.CharField      ( max_length = 32 )
    user_tipe       = models.CharField      ( max_length = 1  )
    user_ativo      = models.CharField      ( max_length = 1, default = 's' )   

class Sessionini(models.Model):
    user_ids        = models.IntegerField   ( default    = 0  )
    token           = models.CharField      ( max_length = 64 )
    user_tipe       = models.CharField      ( max_length = 1  )   
    ativo           = models.BooleanField   ( default = False )
    horaini         = models.IntegerField   ( default = 0     )
    
class HistoryUser(models.Model):
    user_ids        = models.IntegerField   ( default    = 0  )
    hora            = models.CharField      ( max_length = 17 )
    event           = models.CharField      ( max_length = 100)

#CHIP
class Chip(models.Model):
    chip_ip         = models.CharField      ( max_length = 45 )
    chip_num        = models.CharField      ( max_length = 8  )
    chip_oper       = models.CharField      ( max_length = 15 )
    chip_data       = models.CharField      ( max_length = 17 )
    chip_ativo      = models.CharField      ( max_length = 1, default = 's' )
    chip_where      = models.CharField      ( max_length = 1, default = 'e' )# e= estoque s= saida m= modulo
    chip_whedes     = models.IntegerField   ( default    = 0  )# quem qual

class EntradaChipEstoque(models.Model):
    chip_id         = models.IntegerField   ( default    = 0  )
    chip_data       = models.CharField      ( max_length = 17 )
    entradapor      = models.CharField      ( max_length = 45 )
    event           = models.CharField      ( max_length = 100)

class ChipSaidas(models.Model):
    chip_id         = models.IntegerField   ( default    = 0  )
    chip_data       = models.CharField      ( max_length = 17 )
    saida_autorz    = models.CharField      ( max_length = 45 )
    saida_para      = models.CharField      ( max_length = 45 )    

class HistoryChip(models.Model):
    chip_id         = models.IntegerField   ( default    = 0  )
    hora            = models.CharField      ( max_length = 17 )
    event           = models.CharField      ( max_length = 100)

#EMPRESA
class Empresas(models.Model):
    emp_nome        = models.CharField      ( max_length = 12 )
    empdata_cnpj    = models.CharField      ( max_length = 18 )
    empdata_email   = models.CharField      ( max_length = 60 )
    empdata_razao   = models.CharField      ( max_length = 90 )
    empdata_resp    = models.CharField      ( max_length = 45 )
    empdata_tel     = models.CharField      ( max_length = 14 )

    end_bairro      = models.CharField      ( max_length = 45 )
    end_cep         = models.CharField      ( max_length = 45 )
    end_cidade      = models.CharField      ( max_length = 45 )
    end_comp        = models.CharField      ( max_length = 45 )
    end_num         = models.CharField      ( max_length = 45 )
    end_ref         = models.CharField      ( max_length = 45 )
    end_rua         = models.CharField      ( max_length = 60 )
    end_uf          = models.CharField      ( max_length = 2  )

    cont_On         = models.CharField      ( max_length = 3  )   
    cont_Tot        = models.CharField      ( max_length = 3  )   
    emp_ativo       = models.BooleanField   ( default =  True )  

class HistoryEmpresas(models.Model):
    ids             = models.IntegerField   ( default = 0     )
    hora            = models.CharField      ( max_length = 17 )
    event           = models.CharField      ( max_length = 100)
