from rest_framework import serializers
from .models import Photo
from git.serializers import FileInfoSerializer


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id','title','size','width','height']
        read_only_fields = ['user', 'original', 'thumbnail']