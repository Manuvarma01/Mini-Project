"""CourtCaseManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from ccms.views import login, lawyerregistration, clientregistration, getlawyers, activateAccount, logout, postCase, \
    postCaseAction, getcases, deleteCase, updatecase, updatecaseaction, uploaddocument, \
    uploaddocumentaction, getdocuments, deletedocuments, postAppointment, postAppointmentAction, getappointments, \
    deleteAppointment, updateappointment, updateappointmentaction, acceptorrejectcase

urlpatterns = [

    path('admin/', admin.site.urls),
	
	path('', TemplateView.as_view(template_name='index.html'), name='login'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='login'),
    path('loginaction/', login, name='loginaction'),

    path('lawyerregistration/', TemplateView.as_view(template_name='lawyerregistration.html'), name='registration'),
    path('lawyerregaction/', lawyerregistration, name='regaction'),

    path('clientregistration/', TemplateView.as_view(template_name='clientregistration.html'), name='registration'),
    path('clientregaction/', clientregistration, name='regaction'),

    path('logout/', logout, name='logout'),

    path('getlawyers/', getlawyers, name='getlawyers'),

    path('activateAccount/', activateAccount, name='activateAccount'),

    #=========================================================================================

    path('postCase/',postCase,name='post'),
    path('postCaseAction/',postCaseAction, name='postCaseAction'),
    path('getcases/', getcases, name='getcases'),
    path('deleteCase/', deleteCase, name='deleteCase'),
    path('updatecase/', updatecase, name='updatecase'),
    path('updatecaseaction/', updatecaseaction, name='updatecaseaction'),
    path('acceptorrejectcase/', acceptorrejectcase , name='acceptorrejectcas'),

    #============================================================================================

    path('uploaddocument/', uploaddocument, name=''),
    path('uploaddocumentaction/', uploaddocumentaction, name=''),
    path('getdocuments/', getdocuments, name=''),
    path('deletedocuments/', deletedocuments, name=''),

    #===============================================================================================

    path('postAppointment/', postAppointment, name=''),
    path('postAppointmentAction/', postAppointmentAction, name=''),
    path('getappointments/', getappointments, name=''),
    path('deleteAppointment/',deleteAppointment, name=''),
    path('updateappointment/', updateappointment, name=''),
    path('updateappointmentaction/', updateappointmentaction, name=''),

    #==================================================================================================
]
