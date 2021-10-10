from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'published_date', 'author', 'summary', 'content']
