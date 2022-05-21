
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=255,null=True)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.fname

class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=200,null=True)
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    sid=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.fname

class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=200,null=True)
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.fname

class Course(models.Model):
    cid=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    depcode=models.CharField(max_length=200,null=True)
    sem=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    deptcode=models.CharField(max_length=200,null=True)
    deptname=models.CharField(max_length=200,null=True)
        
    def __str__(self):
        return self.deptname

class Course_Outcome(models.Model):
    co_no=models.IntegerField(default=0,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True)
    cog_lvl=models.IntegerField(default=0,null=True,blank=True)
        
    def __str__(self):
        return self.desc

class Program_Outcome(models.Model):
    po_no=models.IntegerField(default=0,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True)
        
    def __str__(self):
        return self.desc

class Program_Specific_Outcome(models.Model):
    pso_no=models.IntegerField(default=0,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True)
        
    def __str__(self):
        return self.desc

        

