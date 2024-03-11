from rest_framework import serializers
from .models import FileId

class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=FileId
        fields=['name','size']