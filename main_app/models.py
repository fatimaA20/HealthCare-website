from django.db import models
from django.contrib.auth.models import  AbstractUser , BaseUserManager, PermissionsMixin
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from datetime import datetime


# Create your models here.


SHIFTS = (
    ('1', 'Early Morning'),
    ('2', 'Late Morning'),
    ('3', 'Evening'),
)

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

#  this well allow you to add more parameters in user model 
class CustomUser (AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLES , default='patient')  
    mobile_Number = models.CharField(max_length=5000, default="0000")
    image = models.ImageField(upload_to='main_app/static/images/users',default='default.jpg') 


class Patient(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile', null=True ) 
    blood = models.CharField(max_length=100 , null=True)
    cpr = models.CharField(max_length=100 , null=True)
    height = models.FloatField(max_length=5, null=True)
    weight = models.FloatField(max_length=5, null=True)
    dof = models.DateField(max_length=100, null=True)
    sensitivity = models.TextField(max_length=5000, null=True)




class Department(models.Model):
    name = models.CharField(max_length=50)
    brief = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='main_app/static/images/department',default='') 

    def __str__(self):
        return self.name
    #  for redirecting to toys details page - we use pk because we will use CBV's
    def get_absolute_url(self):
        return reverse('departments_detail', kwargs ={'pk' : self.id})

class Doctor (CustomUser):
    shift = models.CharField(
        max_length=1,
        choices=SHIFTS,
        default=SHIFTS[0][0]  
    )
    description = models.TextField(max_length=5000)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null = True , blank= True)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('doctors_detail', kwargs ={'pk' : self.id})

class appointment (models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null = True , blank= True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.patient} | day: {self.day} | time: {self.time}"
    
    def get_absolute_url(self):
        return reverse('appointments_detail', kwargs ={'pk' : self.id})