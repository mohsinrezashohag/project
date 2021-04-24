from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.shortcuts import redirect
from . models import Doctor_Request
from accounts.models import Doctor,Patient

# Create your views here.


def home (request):

    doctor=Doctor.objects.all()
    context={'doctor':doctor}
    return render(request,'pages/index.html',context)






def doctor_profile(request,user_id):


    profile=get_object_or_404(Doctor, pk=user_id)
    context={'profile':profile}
    return render(request,'pages/doctor_profile.html',context)



def doctors_search(request):

    doctor=Doctor.objects.all()
    total_doctor=doctor.count()
    context={'doctor':doctor,'total_doctor':total_doctor}
    return render(request,'pages/doctors_search.html',context)










def search_result(request):

    search=request.GET['search']


    searched_doctors=Doctor.objects.filter(speciality__icontains=search)

    total_searched_doctors=searched_doctors.count()


  

      

        



    context={'searched_doctors':searched_doctors,'total_searched_doctors':total_searched_doctors}
    return render(request,'pages/search_result.html',context)















def Doctor_contact(request):

   
    if request.method == 'POST':

       doctor_name=request.POST['doctor_name']
       doctor_id=request.POST['doctor_id']
       doctor_speciality=request.POST['doctor_speciality']
       user_id=request.POST['user_id']
       name=request.POST['name']
       email=request.POST['email']
       phone=request.POST['phone']
       message=request.POST['message']
    #    patient_image=request.post['patient_image']
       



       if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Doctor_Request.objects.all().filter(user_id=user_id,doctor_id=doctor_id)

            if has_contacted:
                messages.error(request, 'You have already has contact for this ')
                return redirect('p_dashboard')
        
       
       
       Doctor_contact=Doctor_Request(doctor_name=doctor_name,name=name,email=email,phone=phone,message=message,user_id=user_id,doctor_id=doctor_id,doctor_speciality=doctor_speciality)

       Doctor_contact.save()

       messages.success(request,'Your Request has been submited.We will contact you soon')

       

       return redirect('request_success')






















def about (request):

    return render(request,'pages/about_us.html')



