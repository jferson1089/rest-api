from django.shortcuts import render
from .models import System, Games
from .serializers import SystemSerializer, GameSerializer
from rest_framework import generics


# Create your views here.
class SystemListView(generics.ListAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class SystemCreateView(generics.CreateAPIView):

    def create(self, serializer):
        serializer.save()


class SystemUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class GamesListView(generics.ListAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer


class GamesCreateView(generics.CreateAPIView):

    def create(self, serializer):
        serializer.save()

class GamesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer