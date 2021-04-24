import django
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import PatientCreateForm,DoctorCreateForm
from django.contrib.auth import login,authenticate
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin



from django.views.generic import CreateView

from . models import User,Doctor,Patient
# Create your views here.





class PatientRegistaionView(CreateView):

    model = User
    form_class=PatientCreateForm
    template_name='accounts/p_register.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type']='patient'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
         user=form.save()
         login(self.request,user)
         return redirect('home')





class DoctorRegistaionView(CreateView):

    model = User
    form_class=DoctorCreateForm
    template_name='accounts/d_register.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type']='doctor'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
         user=form.save()
         login(self.request,user)
         return redirect('doctors_dash')



def d_login(request):

    if request.method== 'POST':

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)


        if user is not None :
            auth.login(request,user)
            return redirect ('doctors_dash')

        else:
            return HttpResponse("vul information")


    else:

         return render(request,'accounts/d_login.html')



def p_login(request):

    if request.method== 'POST':

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)


        if user is not None :
            auth.login(request,user)
            return redirect ('p_dashboard')

        else:
            return HttpResponse("vul information")


    else:

         return render(request,'accounts/p_login.html')










def logout(request):

    auth.logout(request)

    return redirect('home')