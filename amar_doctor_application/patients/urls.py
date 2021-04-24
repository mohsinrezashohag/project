from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    
    path('p_dashboard/',views.p_dashboard,name='p_dashboard'),
    path('p_chat/',views.p_chat,name='p_chat'),
    path('pescription_show/',views.pescription,name='pescription_show'),
    path('request_success/',views.request_success,name='request_success'),
]