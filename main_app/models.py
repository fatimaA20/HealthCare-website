from django.db import models
from django.contrib.auth.models import  AbstractUser , BaseUserManager, PermissionsMixin
from django.urls import reverse

# Create your models here.


SHIFTS = (
    ('1', 'Early Morning'),
    ('2', 'Late Morning'),
    ('3', 'Evening'),
)

#  this well allow you to add more parameters in user model 
class CustomUser (AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLES)
    mobile_Number = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='main_app/static/images/users',default='default.jpg') 



class Patient (CustomUser):
    blood = models.CharField(max_length=100)
    cpr = models.CharField(max_length=100)
    height = models.FloatField(max_length=5)
    weight = models.FloatField(max_length=5)
    dof = models.DateField(max_length=100)
    sensitivity = models.TextField(max_length=5000)
   

class Department(models.Model):
    name = models.CharField(max_length=50)
    brief = models.TextField(max_length=50)
    image = models.ImageField(upload_to='main_app/static/images/department',default='') 

    def __str__(self):
        return self.name
    #  for redirecting to toys details page - we use pk becuse we will use CBV's
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
    
    def get_absolute_url(self):
        return reverse('doctors_detail', kwargs ={'pk' : self.id})


class appointment (models.Model):
    start_time =models.TimeField(null = True , blank= True)
    end_time =models.TimeField( null = True , blank= True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)