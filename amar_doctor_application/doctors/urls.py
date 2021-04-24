from django.urls import path
from . import views

urlpatterns = [
    
    path('doctors_dash/',views.doctors_dash,name='doctors_dash'),
    path('appointments/',views.appointments,name='appointments'),
    path('patients_list/',views.patients_list,name='patients_list'),
    path('dc_register/',views.dc_register,name='dc_register'),
    path('dc_chat/',views.dc_chat,name='dc_chat'),
    path('p_profile/<int:id>/',views.p_profile,name='p_profile'),
    path('appointment_delete/<int:id>/',views.appointment_delete,name='appointment_delete'),
    path('Doctor_contact_approved/<int:id>/',views.Doctor_contact_approved,name='Doctor_contact_approved'),
    path('show_prescription/',views.show_pescription,name='show_pescription'),
    path('create_prescription/',views.create_prescription,name='create_prescription'),
    path('delete/<int:id>/',views.delete,name='delete'),

    
]