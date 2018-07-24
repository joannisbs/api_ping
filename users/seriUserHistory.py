from rest_framework import serializers
from users.models import History

class Historyserial(serializers.Serializer):
    user_ids = serializers.IntegerField(default=0)
    hora     = serializers.CharField(max_length=17)
    event    = serializers.CharField(max_length=100)

    def Save(self,data):
        return History.objects.create(**data)