from django.db import models
from django.contrib.auth.models import User
from git.models import FileInfo

class Photo(models.Model):
    width=models.IntegerField()
    height=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    original=models.ForeignKey(FileInfo, on_delete=models.CASCADE)
    thumbnail=models.ForeignKey(FileInfo, on_delete=models.CASCADE)