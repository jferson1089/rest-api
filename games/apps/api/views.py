from django.shortcuts import render
from .models import System, Games
from .serializers import SystemSerializer, GameSerializer
from rest_framework import generics


# Create your views here.
class SystemListView(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

    def perform_create(self, serializer):
        serializer.save()
#
# class SystemCreateView(generics.CreateAPIView):


class SystemUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class GamesListView(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()





# class GamesCreateView(generics.CreateAPIView):


class GamesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer