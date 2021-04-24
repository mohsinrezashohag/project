from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from pages.models import Doctor_Request

from doctors.models import Pescription
# Create your views here.





def p_dashboard(request):


    
    all_patient=Doctor_Request.objects.filter(name=request.user.username)
    id=request.user.id
    press=Pescription.objects.all()
    
    # filter(patient=request.user.id)



    context={'all_patient':all_patient,'press':press}
    return render(request,'patients/p_dashboard.html',context)
 












def p_chat(request):
    return render(request,'patients/chat.html')






from doctors.models import Pescription


def pescription(request):
    presscription=Pescription.objects.filter(patient=request.user.id)
    
    context={'presscription':presscription}
    return render(request,'patients/pescription_show.html',context)



def request_success(request):
    return render(request,'patients/request_success.html')


