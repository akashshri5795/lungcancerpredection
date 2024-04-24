import os
from uuid import uuid4
from django.db import models

class PatientModel(models.Model):
    patient_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=1)
    contact=models.CharField(max_length=10)   
    address=models.TextField()


def custom_upload_path(instance, filename):   
    ext = filename.split('.')[-1] 
    filename = f"{uuid4().hex}.{ext}" 
    return os.path.join("CTscan", filename)


class PatientCTScans(models.Model):    
    patient_id = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    upload_image=models.FileField(upload_to=custom_upload_path, max_length=100, verbose_name="Upload Image")
    upload_date=models.DateTimeField(auto_now_add=True)
    

