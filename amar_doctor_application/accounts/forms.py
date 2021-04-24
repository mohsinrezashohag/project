from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . models import Doctor,Patient
from django.contrib.auth import get_user_model
User = get_user_model()




class PatientCreateForm(UserCreationForm):
    
    email=forms.EmailField(required=True)
    phone=forms.IntegerField(required=True)
    age=forms.IntegerField(required=True)
    profile_pic=forms.ImageField()
    




    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email',)

        labels={
              'username': 'Your Name',
              'email': 'Your Email',
              'password': 'Type your Password ',
             
              
              }
        



    @transaction.atomic
    def save(self):

        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_patient=True
        user.save()
        patient=Patient.objects.create(user=user)
        patient.phone=self.cleaned_data.get('phone')
        patient.age=self.cleaned_data.get('age')
        patient.email=self.cleaned_data.get('email')
        patient.profile_pic=self.cleaned_data.get('profile_pic')

        patient.save()
        return user




class DoctorCreateForm(UserCreationForm):
    depertment={

     ('Urology','Urology'),
     ('Neurology','Neurology'),
     ('Orthopedic','Orthopedic'),
     ('Cardiologist','Cardiologist'),
     ('Dentist','Dentist'),
    }
    email=forms.EmailField(required=True)
    degre=forms.CharField(max_length=200, required=True)
    speciality=forms.ChoiceField(choices=depertment)
    profile_image=forms.ImageField()
    
    
    



    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):

        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_doctor=True
        user.save()
        doctor=Doctor.objects.create(user=user)
        doctor.degre=self.cleaned_data.get('degre')
        doctor.speciality=self.cleaned_data.get('speciality')
        doctor.profile_image=self.cleaned_data.get('profile_image')
        doctor.save()
        return user
