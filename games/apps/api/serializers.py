from rest_framework import serializers
from .models import System, Games

class SystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = System
        fields = ('name', 'company', 'price', 'production')

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Games
        fields = ('title', 'year', 'developer', 'system')