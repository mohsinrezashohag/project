
from django.db import models
from pages.models import Doctor_Request
from accounts.models import Patient
# Create your models here.



class  Pescription(models.Model):


   #   patient=models.ForeignKey(Doctor_Request,on_delete=models.CASCADE,null=True)
     patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
     medicine_name=models.CharField(max_length=50,null=True)
     take_time=models.CharField(max_length=50,null=True)
     medical_suggestion=models.CharField(max_length=200,null=True)

     def patient_name(self):

        return self.patient.user

     def __str__(self):
        
        return str(self.patient.user)


      



