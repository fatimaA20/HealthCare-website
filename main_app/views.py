from django.shortcuts import render , redirect
from .models import Department ,Doctor , Profile
# this should be used to class based
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# here no edit bcz it just return data from database - No change in DB
from django.views.generic import ListView , DetailView
# these 2 lines was imported to create form of signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Make a 'user' form object with the data from the browser
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save user to DB
            user = form.save()
            # Log in the user automatically once they sign up
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid: Please Try Again!'
    # If there's a bad post or get request
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Departments CBV's
class DepartmentsList(ListView):
  model = Department

class DepartmentsDetail(DetailView):
  model = Department

class DepartmentsCreate(CreateView):
  model = Department
  # fields = '__all__'
  fields = ['name','brief']


class DepartmentsUpdate(UpdateView):
  model = Department
  fields = '__all__'

class DepartmentsDelete(DeleteView):
  model = Department
  success_url = '/departments/'


# Doctor CBV's
class DoctorsList(ListView):
  model = Doctor,Profile

class DoctorsDetail(DetailView):
  model = Doctor

class DoctorsCreate(CreateView):
  model = Doctor
  # profile = Profile.objects.filter()
  fields = '__all__'

class DoctorsUpdate(UpdateView):
  model = Doctor
  fields = '__all__'

class DoctorsDelete(DeleteView):
  model = Doctor
  success_url = '/doctors/'