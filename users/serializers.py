from rest_framework import serializers
from users.models import User

class UserSerializer (serializers.Serializer):
    id        = serializers.IntegerField(read_only=True)
    user_nome = serializers.CharField(max_length=45)
    user_pass = serializers.CharField(max_length=32)
    user_tipe = serializers.CharField(max_length=1)   

    def Desmonta(self,instance):

        instance.user = instance.get('user')
        instance.word = instance.get('pass')
        return instance
    
    def Authentic(self, value, psw):
        res = User.objects.filter(user_nome=value)
        for re in res:
            pswli =  re.user_pass
        if pswli == psw:
            return [True,re.user_tipe]
        else:
            return [False,'nothing']