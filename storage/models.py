from django.db import models
from django.contrib.auth.models import User
from git.models import FileId

class Folder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    inside = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

class File(models.Model):
    title = models.CharField(max_length=255)
    size=models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    inside = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.SET_NULL)
    fileId=models.ForeignKey(FileId,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)