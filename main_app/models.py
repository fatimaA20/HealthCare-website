from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


SHIFTS = (
    ('1', 'Early Morning'),
    ('2', 'Late Morning'),
    ('3', 'Evening'),
)

class Profile (models.Model):
    user_role = models.CharField(max_length=100)
    mobile_Number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='main_app/static/images/users',default='') 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="user_contact"
    )    

class Patient (models.Model):
    blood = models.CharField(max_length=100)
    cpr = models.CharField(max_length=100)
    height = models.FloatField(max_length=5)
    weight = models.FloatField(max_length=5)
    dof = models.DateField(max_length=100)
    sensitivity = models.TextField(max_length=5000)
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,

    )    

class Department(models.Model):
    name = models.CharField(max_length=50)
    brief = models.CharField(max_length=50)
    image = models.ImageField(upload_to='main_app/static/images/department',default='') 

    def __str__(self):
        return self.name
    #  for redirecting to toys details page - we use pk becuse we will use CBV's
    def get_absolute_url(self):
        return reverse('departments_detail', kwargs ={'pk' : self.id})

class Doctor (models.Model):
    shift = models.CharField(
        max_length=1,
        choices=SHIFTS,
        default=SHIFTS[0][0]  
    )
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
    )    
    description = models.TextField(max_length=5000)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')

    def get_absolute_url(self):
        return reverse('doctors_detail', kwargs ={'pk' : self.id})

class appointment (models.Model):
    start_time:models.TimeField()
    end_time:models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)