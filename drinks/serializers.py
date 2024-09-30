from rest_framework import serializers

from .models import Drinks, User

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','drink_name','drink_description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'