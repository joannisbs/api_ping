from rest_framework import serializers
from users.models import Chip

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