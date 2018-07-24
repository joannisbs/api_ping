from rest_framework import serializers
from users.models import Sessionini


class Session(serializers.Serializer):
    user_ids   = serializers.IntegerField(default=0)
    token     = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)   
    ativo     = serializers.BooleanField(default=False)
    horaini   = serializers.IntegerField(default=0)


    def createSession(self, data, ids):
        limp = Sessionini.objects.filter(ativo=False)
        for lipr in limp:
            lipr.delete()

        res = Sessionini.objects.filter(user_ids=ids,ativo=True)
        for re in res:
            re.ativo = False
            re.delete()
        return Sessionini.objects.create(**data)
