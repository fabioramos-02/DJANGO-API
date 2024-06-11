from rest_framework import serializers

from .models import User
#importar serializers do rest_framework
#criar uma classe com o nome UserSerializer(serializers.ModelSerializer)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'