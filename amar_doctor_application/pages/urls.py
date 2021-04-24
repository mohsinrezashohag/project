from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('doctors_search/',views.doctors_search,name='doctors_search'),
    path('search_result/',views.search_result,name='search_result'),
    path('doctor_profile/<int:user_id>/',views.doctor_profile,name='doctor_profile'),
    path('doc_contact/',views.Doctor_contact,name='doc_contact')

]