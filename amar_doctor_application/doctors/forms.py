from django import forms
from pages.models import Doctor_Request
from . models import Pescription

class approval_form(forms.ModelForm):
    
    class Meta:
        model = Doctor_Request
        fields = ('confirm',)


        labels={
              'confirm': 'Approved',
            
              }




class PescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Pescription
        fields = ('patient','medicine_name','take_time','medical_suggestion')


        labels={
              'patient': 'Patient Name :',
              'medicine_name': 'Medicine Name :',
              'take_time': 'Medicine Need To Take :',
              'medical_suggestion': 'Suggetion to the patient :',         
             
              }


        