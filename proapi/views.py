from django.shortcuts import render
from rest_framework.response import Response
from .json import jsonstudent
from rest_framework.views import APIView
from .models import student
# Create your views here.



class student_list(APIView):
    def get(self,request):
        s1=student.objects.all()
        s2=jsonstudent(s1,many=True)
        return Response(s2.data)







def index(request):

    return render(request,'main.html',{'key':'hello werdani and welcom'})