from django.db import models
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.contrib.admin import widgets
from django.urls import reverse
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
from django.contrib.auth.models import User


# Create your models here.
shift=(('Morning','morning'),('Afternoon','Afternoon'),('Evening','Evening'))
Hostel=()
for i in range(18):
    hostel_no='Hostel'+" "+str(i+1),'Hostel'+" "+str(i+1)
    hostel_noS=hostel_no,
    Hostel=Hostel+hostel_noS
Roomno=()
for i in range(101,500):
   room_no ='Room no:'+str(i),'Room no:'+' '+str(i)
   roomnos=room_no,
   Roomno +=roomnos

    







class cleaning(models.Model):
    hostel=models.CharField(null=True,max_length=20,choices=Hostel)
    room=models.CharField(null=True,max_length=20)
    Cleaning_done=models.BooleanField(null=True,default=False)
    
    Contact_number=models.CharField(null=True,max_length=20)
    date=models.DateField("Date of cleaning",null=True,)
    time=models.TimeField("Time of cleaning",null=True,)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    timeapply=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('hostel','date','time')
    def __str__(self):
        return self.hostel
    def get_absolute_url(self):
        return reverse("cleaningdetail-page", kwargs={"pk": self.pk})
class wingcleaning(models.Model):
    hostel=models.CharField( max_length=50,choices=Hostel)
    Room=models.CharField("Any Room no. of the Wing",max_length=20)
    shift=models.CharField(max_length=20,choices=shift)
    timeapply=models.DateTimeField(auto_now_add=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "Hostel no.:"+self.hostel +" Wing no:" +self.Room
    
    def get_absolute_url(self):
        return reverse("wingcleaningdetail-page", kwargs={"pk": self.pk})
