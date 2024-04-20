from django.db import models

# Create your models here.
class userAccount(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    
