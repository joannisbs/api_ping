from rest_framework        import serializers
from users.models          import HistoryChip
from users.getTime         import GetTime

class HistoryChipSerializer(serializers.Serializer):
    chip_id         = serializers.IntegerField(default=0)
    hora            = serializers.CharField(max_length=17)
    event           = serializers.CharField(max_length=100)

    def insert(self,data):
        HistoryChip.objects.create(**data)

def AdcionaHistoryChip(chip_id,mensage):
    t = GetTime()
    time = t.get_full_db
    obj = HystoryObj(chip_id,time,mensage)
    obj = HistoryChipSerializer(obj)
    obj.insert(obj.data)

    print mensage

class HystoryObj:
    def __init__(self,ids,hora,event):
        self.chip_id    = ids
        self.hora       = hora
        self.event      = event