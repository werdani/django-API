"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from proapi import views
from rest_framework import routers


a=routers.DefaultRouter()
a.register('',views.student_list1)

b=routers.DefaultRouter()
b.register('',views.doctorjson)

c=routers.DefaultRouter()
c.register('',views.user_json)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('studentjson/',views.student_list.as_view(),name='studentjson'),
    path('student/',include(a.urls)),
    path('doctor/',include(b.urls)),
    path('user/',include(c.urls)),
    path('data/',views.getdata),
]
