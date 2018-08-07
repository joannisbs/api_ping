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