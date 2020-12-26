"""InstituteWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from InstituteWebApp.view import getStudentDetails
from InstituteWebApp import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',getStudentDetails, name='getStudentDetails'),
    url(r'^getFacultyDetails/$',view.getFacultyDetails, name='getFacultyDetails'),
    url(r'^add_student/$', view.add_student, name='add_student'),
    url(r'^add_menu/$', view.add_menu, name='add_menu'),
    url(r'^getMenuDetails/$', view.getMenuDetails, name='getMenuDetails')



]
