from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField(default="no description", blank=True)
    color=models.CharField(max_length=20,default='#dcdcdc')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)