
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.safestring import  mark_safe  
from PIL import Image





class User(AbstractUser):

    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
   
   
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    profile_pic=models.ImageField(default="d.png",upload_to='uploded_image/')
    def imageURL(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return " "



        

    


    def __str__(self):
        return self.user.username or ''

class Doctor(models.Model):
    depertment={

   ('Urology','Urology'),
   ('Neurology','Neurology'),
   ('Orthopedic','Orthopedic'),
   ('Cardiologist','Cardiologist'),
   ('Dentist','Dentist'),
 
    }
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_image=models.ImageField(default="d.png",upload_to='uploded_image/')
    degre=models.CharField(max_length=50,null=True)
    speciality=models.CharField(max_length=200,null=True,choices=depertment)
    def imageURL(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return " "

    


    def image_show(self):

        if self.profile_image:

            return mark_safe('<img src="{}" width="70"  />'.format(self.profile_image.url))  
        return ""

    



    def __str__(self):
        return self.user.username or ''

    