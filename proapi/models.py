from django.db import models

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    date_re=models.DateField()
    degree=models.IntegerField()
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lname


class doctor(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    date_re=models.DateField()
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lname
    