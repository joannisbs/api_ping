from rest_framework import serializers
from users.models import Chip , HistoryChip 
from users.models import EntradaChipEstoque

class Post_CreateChip(serializers.Serializer):
    chip_ip       = serializers.CharField(max_length=45)
    chip_num      = serializers.CharField(max_length=8)
    chip_oper     = serializers.CharField(max_length=15)
    chip_data     = serializers.CharField(max_length=17)
    chip_ativo    = serializers.CharField(max_length=1, default='s')
    chip_where    = serializers.CharField(max_length=1, default='e')# e=estoque s=saida m=modulo
    chip_whedes   = serializers.IntegerField(default=0)# quem qual

    def Save(self,data):
        try:
            Chip.objects.create(**data)
            return True
        except:
            return False

class Post_ChipHistoryDbSeri (serializers.Serializer):
    chip_id = serializers.IntegerField(default=0)
    hora     = serializers.CharField(max_length=17)
    event    = serializers.CharField(max_length=100)

    def Save(self,data):
        
        return HistoryChip.objects.create(**data)

class Post_ChipToEstoque (serializers.Serializer):
    chip_id       = serializers.IntegerField(default=0)
    chip_data     = serializers.CharField(max_length=17)
    entradapor    = serializers.CharField(max_length=45)
    event         = serializers.CharField(max_length=100)

    def Save(self,data):
        
        return EntradaChipEstoque.objects.create(**data)