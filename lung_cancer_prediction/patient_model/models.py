from django.db import models

class PatientModel(models.Model):
    patient_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=1)
    contact=models.CharField(max_length=10)   
    address=models.TextField()
