from django.shortcuts import render
import rest_framework
from .serializers import ContentSerializer
from .models import Content, PUBLISHED
from rest_framework import generics


class ContentView(generics.ListAPIView):
    queryset = Content.objects.filter(status=PUBLISHED)
    serializer_class = ContentSerializer
