from rest_framework import serializers
from django.contrib.auth.models import User
from .models import student ,doctor


class jsonstudent(serializers.ModelSerializer):
    class Meta:
         model = student
         fields= '__all__'


class jsondoctor(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = '__all__'


class json_user(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    

    

