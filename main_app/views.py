from django.shortcuts import render, redirect
from .models import Department, Doctor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Home view
def home(request):
    return render(request, 'home.html')

# Signup view
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Create a 'UserCreationForm' object with the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save user to the database
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

# Departments class-based views
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

# Doctor class-based views
class DoctorsList(ListView):
    model = Doctor

class DoctorsDetail(DetailView):
    model = Doctor

class DoctorsCreate(CreateView):
    model = Doctor
    fields = '__all__'

class DoctorsUpdate(UpdateView):
    model = Doctor
    fields = '__all__'

class DoctorsDelete(DeleteView):
    model = Doctor
    success_url = '/doctors/'