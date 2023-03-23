from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Department ,Doctor , CustomUser ,SHIFTS , appointment , Patient
# this should be used to class based
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# here no edit bcz it just return data from database - No change in DB
from django.views.generic import ListView , DetailView
# these 2 lines was imported to create form of signup
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserChangeForm, PasswordChangingForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy

# for user signup
from .forms import CustomUserCreationForm,AdminProfileForm,PatientProfileForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            patient = Patient(user_id=user.id)  # create Patient object with user attribute
            patient.save()
            print("Call Function")
            update_user(pk=user.id, form_data=request.POST)
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid: Please Try Again!', form.errors, form.error_messages
    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def update_user(pk, form_data):
    print("pk", pk)
    print("form_data", form_data)
    user = CustomUser.objects.get(pk=pk)
    form = CustomUserChangeForm(form_data, instance=user)
    if form.is_valid():
        form.save()

       
   



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
  fields=['first_name','last_name','username','password','email','mobile_Number','description','department']

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

# changing password
class PasswordChangeView(PasswordChangeView):
   form_class = PasswordChangingForm
   success_url = reverse_lazy()
def password_sucess(request):
   return render(request, 'registration/password_change.html')
   
   
   
# def profile_edit(request , user_id):
#    user = CustomUser.objects.get(id=user_id)
#    form = CustomUserChangeForm()
#    return render(request, 'registration/profile_edit.html',{'user' : user , 'form' : form})






def edit_admin_profile(request, user_id):
    User = get_user_model()
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('profile', kwargs={'user_id': user.id}))

    else:
        form = CustomUserChangeForm(instance=user)
        context = {'form': form, 'user': user}
        return render(request, 'registration/edit_admin_profile.html', context)


# edit_doctor_profile
def edit_doctor_profile(request, user_id):
   User = get_user_model()
   user = User.objects.get(id=user_id)
   if request.method == 'POST':
      form = DoctorEditProfileForm(request.POST,request.FILES, instance=user)
      if form.is_valid():
         form.save()
         messages.success(request, 'Profile updated successfully')
         return redirect(reverse('profile', kwargs={'user_id': user.id}))
   else:
        form = DoctorEditProfileForm(instance=user)
   context = {'form': form, 'user': user}
   return render(request, 'registration/edit_doctor_profile.html', context)


def edit_patient_profile(request,user_id):
   User = get_user_model()
   user = User.objects.get(id=user_id)
   if request.method == 'POST':
      form = PatientEditProfileForm(request.POST,request.FILES, instance=user)
      if form.is_valid():
         form.save()
         messages.success(request, 'Profile updated successfully')
         return redirect(reverse('profile', kwargs={'user_id': user.id}))
   else:
        form = PatientEditProfileForm(instance=user)
   context = {'form': form, 'user': user}
   return render(request, 'registration/edit_doctor_profile.html', context)







# Departments CBV's
## Departments CBV's
class AppointmentsList(ListView):
  model = appointment


class AppointmentsDetail(DetailView):
  model = appointment


class AppointmentsCreate(CreateView):
  model = appointment
  fields = ['department' , 'doctor' , 'day' , 'time']
  # fields = '__all__'
  def form_valid(self, form):
    form.instance.patient_id = self.request.user.id
    return super().form_valid(form)

  


class AppointmentsUpdate(UpdateView):
  model = appointment
  fields = '__all__'


class AppointmentsDelete(DeleteView):
  model = appointment
  success_url = '/appointments/'   

def DepartmentDoctor(request, department_id):
   doctors = Doctor.objects.filter(department_id=department_id)
   department = Department.objects.get(id=department_id)
   return render(request, 'main_app/department_doctor.html', {'doctors': doctors, 'department': department})


# this reset password 
