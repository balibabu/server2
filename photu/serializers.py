from rest_framework import serializers
from .models import Photo
from git.serializers import FileInfoSerializer


class PhotoSerializer(serializers.ModelSerializer):
    original = FileInfoSerializer(read_only=True)
    thumbnail = FileInfoSerializer(read_only=True)
    class Meta:
        model = Photo
        fields = ['id','width','height', 'original', 'thumbnail']
        read_only_fields = ['user', 'original', 'thumbnail']