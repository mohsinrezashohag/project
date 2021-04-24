from django import forms
from .models import Doctor_Request


class approval_form(forms.ModelForm):
    
    class Meta:
        model = Doctor_Request
        fields = ('confirm',)


        labels={
              'confirm': 'Approved',
            
              }