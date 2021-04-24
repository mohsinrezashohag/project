from django.urls import path
from . import views
from . views import *

urlpatterns = [
    
    # path('login/',views.login,name='login'),
    path('p_reg/',PatientRegistaionView.as_view(),name='p_reg'),
    path('d_reg/',DoctorRegistaionView.as_view(),name='d_reg'),
    path('d_login/',views.d_login,name='d_login'),
    path('p_login/',views.p_login,name='p_login'),
    path('logout/',views.logout,name='logout'),
 ]