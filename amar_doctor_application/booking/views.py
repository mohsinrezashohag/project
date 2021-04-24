# from django.http import request
# from django.http.response import HttpResponse
# from . models import Booking
# from django.shortcuts import render,redirect
# from django.forms import inlineformset_factory
# from accounts.models import Doctor,Patient
# from django.contrib import messages
# from . forms import bookingForm

# # from . forms import bookingForm 
# # from . import forms
# from django.views.generic import CreateView





# def booking_view(request):

#     bookin_form=bookingForm


#     if request.method=="POST":

     
      
#       bookin_form=bookin_form(request.POST)



#       if bookin_form.is_valid():

#         bookin_form.save()

#     context={'bookin_form':bookin_form}
#     return render(request,'booking/dc_book_form.html',context)



   


   



# # def booking_view(request):

# #      if request.method == 'POST':

# #          dc=request.POST['dc']
# #          contacted_date=request.POST['contacted_date']
# #          note=request.POST['note']
        
        
# #          if request.user.is_authenticated:
# #             dc = request.user.dc
# #             has_booked=Booking.objects.all().filter(dc=dc)

# #             if has_booked:
# #                 messages.error(request, 'You have already has contact for this ')
# #                 return redirect('p_dashboard')


# #          booked=Booking(dc=dc,note=note,contacted_date=contacted_date)

# #          booked.save()
         



# #      return redirect('p_dashboard')

