from django.db import models
from datetime import datetime


# Create your models here.



class Doctor_Request(models.Model):


    doctor_id=models.IntegerField(null=True)
    doctor_name=models.CharField(max_length=50)
    doctor_speciality=models.CharField(max_length=50,null=True)
    user_id=models.IntegerField(null=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    confirm=models.BooleanField(default=False)
    
    patient_image=models.ImageField(default="d.png",upload_to='uploded_image/')
   
    def __str__(self) :
        return self.name