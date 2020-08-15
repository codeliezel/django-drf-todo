from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from .models import NoteModel

class NoteSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    tags = ArrayField(
        serializers.CharField(max_length=300), default=list)

    class Meta:
        model = NoteModel
        fields = ['title', 'description', 'tags']    