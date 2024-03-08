from rest_framework import serializers
from .models import Folder, File
from git.serializers import FileInfoSerializer

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Folder
        fields=['id','title','inside']
        read_only_fields = ['user']
        
class FileSerializer(serializers.ModelSerializer):
    file_info = FileInfoSerializer(source='fileInfo', read_only=True)
    class Meta:
        model = File
        fields = ['id', 'timestamp', 'file_info','inside']
        read_only_fields = ['user','fileInfo']