from django.db import models

# Create your models here.
#table for storing the data from contact us page

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)