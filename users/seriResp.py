from rest_framework import serializers
import seriMethodos
from users.models import Sessionini
from getTime import GetTime

class RespLogin(serializers.Serializer):
    token  = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=6)
    nivel  = serializers.CharField(max_length=1)
    ids    = serializers.CharField(max_length=10)
    user   = serializers.CharField(max_length=45)

    def ValidaSession(self, data):
        ids   = data.get('ids') 
        token = data.get('token')
        nivel = data.get('nivel')
        user  = data.get('user')
        tokenses = seriMethodos.GeraTokenSession(token,nivel,user)
        
        res = Sessionini.objects.filter(user_ids = ids,ativo=True)
        
        t = GetTime()
        time = t.get_TimeInMinuts()
        time = str(time)
        time = long(time)

        for re in res:
            if re.token == tokenses:
                if time - re.horaini > 720:
                    re.ativo = [False,0]
                    return [False,0] 
                return [True,ids]
        return [False,0]