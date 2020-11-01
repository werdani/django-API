from django.shortcuts import render
from rest_framework.response import Response
from .json import jsonstudent , jsondoctor,json_user 
from rest_framework.views import APIView
from .models import student , doctor
from django.contrib.auth.models import User 
from rest_framework import viewsets
import requests 
# Create your views here.



class student_list(APIView):
    def get(self,request):
        s1=student.objects.all()
        s2=jsonstudent(s1,many=True)
        return Response(s2.data)
    def post(self):
        pass


# an other way   .
class student_list1(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = jsonstudent 


class doctorjson(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = jsondoctor 

class user_json(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = json_user



def index(request):
    return render(request,'main.html',{'key':'hello werdani and welcom'})



def getdata(request):
    addres='http://ammarwerdani.pythonanywhere.com/doctor/'
    dataa=requests.get(addres).json()
    print(dataa)
    return render (request,'da.html',{'doc':dataa})