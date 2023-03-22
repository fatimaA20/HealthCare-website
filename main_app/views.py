from django.shortcuts import render , redirect
from .models import Department ,Doctor , CustomUser ,SHIFTS
# this should be used to class based
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# here no edit bcz it just return data from database - No change in DB
from django.views.generic import ListView , DetailView
# these 2 lines was imported to create form of signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserChangeForm
from django.http import HttpResponseRedirect,HttpResponse

# for user signup
from .forms import CustomUserCreationForm


# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid: Please Try Again!'
    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Departments CBV's
class DepartmentsList(ListView):
  model = Department


class DepartmentsDetail(DetailView):
  model = Department


class DepartmentsCreate(CreateView):
  model = Department
  fields = '__all__'



class DepartmentsUpdate(UpdateView):
  model = Department
  fields = '__all__'


class DepartmentsDelete(DeleteView):
  model = Department
  success_url = '/departments/'


# Doctor CBV's
class DoctorsList(ListView):
  model = Doctor


class DoctorsDetail(DetailView):
  model = Doctor


class DoctorsCreate(CreateView):
  model = Doctor
  fields=['first_name','last_name','username','password','email','mobile_Number','shift','description','department']

  def form_valid(self, form):
        form.instance.user_role = 'Doctor'  # set the default value for user_role
        return super().form_valid(form)
  

  
  success_url = '/doctors/'


  
class DoctorsUpdate(UpdateView):
  model = Doctor
  fields =  fields=['image','first_name','last_name','username','password','email','mobile_Number','shift','description','department']


class DoctorsDelete(DeleteView):
  model = Doctor
  success_url = '/doctors/'

def profile (request , user_id):
   user = CustomUser.objects.get(id=user_id)
   return render(request, 'registration/profile.html',{'user' : user})
   
# def profile_edit(request , user_id):
#    user = CustomUser.objects.get(id=user_id)
#    form = CustomUserChangeForm()
#    return render(request, 'registration/profile_edit.html',{'user' : user , 'form' : form})


# Appointment
def AppointmentList():
   pass

def BookingAppointment(request, user_id):
   pass

# edit profile
def editProfile(request):
   user = request.user
   if request.method == 'POST':
      form = CustomUserChangeForm(request.POST, instance=user)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/profile/')
      else:
         return render(request, 'registration/edit_profile.html', {'form': form})
      

# def DepartmentDoctor(request):
#     doctors = Doctor.objects.filter(department=request.department_id)
#     return render(request, 'main_app/department_doctor.html', { 'doctors': doctors })


def DepartmentDoctor(request, department_id):
   doctors = Doctor.objects.filter(department_id=department_id)
   department = Department.objects.get(id=department_id)
   return render(request, 'main_app/department_doctor.html', {'doctors': doctors, 'department': department})