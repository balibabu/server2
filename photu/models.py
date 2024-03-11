from django.db import models
from django.contrib.auth.models import User
from git.models import FileId

class Photo(models.Model):
    title = models.CharField(max_length=255)
    width=models.IntegerField()
    height=models.IntegerField()
    size=models.IntegerField()
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    original=models.ForeignKey(FileId, on_delete=models.CASCADE, related_name='original')
    thumbnail=models.ForeignKey(FileId, on_delete=models.CASCADE, related_name='thumbnail')