from rest_framework  import serializers
from users.getTime   import GetTime
from users.models    import History
from users.respostas import objHistory

class Historyserial(serializers.Serializer):
    user_ids = serializers.IntegerField(default=0)
    hora     = serializers.CharField(max_length=17)
    event    = serializers.CharField(max_length=100)

    def Save(self,data):
        return History.objects.create(**data)
    
def CriaHistorico(quem,mensagem):
    t = GetTime()
    time = t.get_full_db()
    obj = objHistory(str(quem),str(time),mensagem)
    obj = Historyserial(obj)
    obj.Save(obj.data)
    return False