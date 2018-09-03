# Imports do Framework:
from rest_framework import serializers

# Imports de Objects
from z_Chip_c0_obj import Resp_newChipObject


def ResponseNewChip_Modal(chip,sucess,motive):
    response = Resp_newChipObject()
    response.sucess = sucess
    response.motivo = motive
    response.number = chip.chip_num
    response.ipaddr = chip.chip_ip
    response = ResponseNewChip_Serializer(response)
    return response.data



class ResponseNewChip_Serializer(serializers.Serializer):
    sucess = serializers.BooleanField(default=False)
    motivo = serializers.CharField(max_length=1)
    ipaddr = serializers.CharField(max_length=45)
    number = serializers.CharField(max_length=8)

class Chip_Serializer(serializers.Serializer):
    id            = serializers.IntegerField(default=0)
    chip_ip       = serializers.CharField(max_length=45)
    chip_num      = serializers.CharField(max_length=8)
    chip_oper     = serializers.CharField(max_length=15)
    chip_data     = serializers.CharField(max_length=17)
    chip_ativo    = serializers.CharField(max_length=1, default='s')
    chip_where    = serializers.CharField(max_length=1, default='e')# e=estoque s=saida m=modulo
    chip_whedes   = serializers.IntegerField(default=0)# quem qual

class ResponseChipDateGeneric_Serializer(serializers.Serializer):
    one = serializers.CharField(max_length=45)
    two = serializers.CharField(max_length=100)
    three = serializers.CharField(max_length=45)