from rest_framework import serializers

from .models import Drinks

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','drink_name','drink_description']