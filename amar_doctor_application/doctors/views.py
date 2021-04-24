from django.shortcuts import render
from pages.models import Doctor_Request
# Create your views here.



def doctors_dash(request):

    all_appointment=Doctor_Request.objects.filter(doctor_name=request.user.username)
    total=all_appointment.count()


    aprooved_appointment=all_appointment.filter(confirm=True)
    
    treatment_ongoing=aprooved_appointment.count()




    context={ 
        'total':total ,     
        'aprooved_appointment':aprooved_appointment ,     
        'treatment_ongoing':treatment_ongoing ,     
            }
    return render (request, 'doctors/dashboard.html',context)

    





from accounts.models import Patient
from django.shortcuts import get_object_or_404



def patients_list(request):


    all_patient=Doctor_Request.objects.order_by('-contact_date').filter(doctor_name=request.user.username)

    context={    
        'all_patient':all_patient,      
        }

    return render (request, 'doctors/patients_list.html',context)




def p_profile(request,id):

    p_profile=get_object_or_404(Doctor_Request,pk=id)

    

    context={'p_profile':p_profile}

    return render (request, 'doctors/p_profile.html',context)



def appointment_delete(request, id):
    work=Doctor_Request.objects.get(pk=id)
    work.delete()
    return redirect('appointments')












def appointments(request):


    all_appointment=Doctor_Request.objects.order_by('-contact_date').filter(doctor_name=request.user.username)
    total=all_appointment.count()
    context={    
        'all_appointment':all_appointment,      
        }

    return render (request, 'doctors/appointment_request.html',context)    




##########################################################################################################################

from django.shortcuts import redirect
from . forms import approval_form
def Doctor_contact_approved(request,id):

    if request.method =="POST":

        patient=get_object_or_404(Doctor_Request,pk=id)
        form=approval_form(request.POST,instance=patient)
        if form.is_valid:

            form.save()

            return redirect('appointments')
    else:

        patient=get_object_or_404(Doctor_Request,pk=id)
        form=approval_form(instance=patient)       
        context={'form':form}
   
        return render(request,'doctors/approval_form.html',context)




    
##########################################################################################################################





def dc_register(request):
    return render(request,'doctors/dc_register.html')


def dc_chat(request):
    return render(request,'doctors/chat.html')








from .models import Pescription
from .forms import PescriptionForm

# Create your views here.


def create_prescription(request):

    if request.method =='POST':

        form=PescriptionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('show_pescription')
    else:   
     form=PescriptionForm()  
    
    context={'form':form}
    return render(request,'doctors/prescription_adding.html',context)






def p_profile(request,id):

    p_profile=get_object_or_404(Doctor_Request,pk=id)

    

    context={'p_profile':p_profile}

    return render (request, 'doctors/p_profile.html',context)










def show_pescription(request):

    pescriopn=Pescription.objects.all()
    

    context={'pescriopn':pescriopn}

    return render(request,'doctors/show_pescription.html',context)










def delete(request, id):

    work=Pescription.objects.get(pk=id)
    work.delete()

    return redirect('show_pescription')
