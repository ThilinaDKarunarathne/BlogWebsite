from django.db import models
from django.shortcuts import render,HttpResponse

# # Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=50)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        
        return 'Message from ' + self.title + ' - ' + self.author
