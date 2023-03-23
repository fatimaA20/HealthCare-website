from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from .models import CustomUser, Doctor,Patient,appointment



class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
            'placeholder':'User Name',
            'maxlength': '50',
            'minlength':'3'

        })
        self.fields['first_name'].widget.attrs.update({
            'required':'',
            'name': 'firstname',
            'type':'text',
            'class':'form-control',
            'placeholder':'first Name',
            'maxlength': '50',
            'minlength':'3'

        })
        
        self.fields['last_name'].widget.attrs.update({
            'required':'',
            'name': 'lastname',
            'type':'text',
            'class':'form-control',
            'placeholder':'last Name',
            'maxlength': '50',
            'minlength':'3'

        })
        
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name': 'email',
            'type':'email',
            'class':'form-control',
             'placeholder':'Email',
             'maxlength': '128',
             'minlength':'6'
        })

        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name': 'password',
            'type':'password',
            'class':'form-control',
             'placeholder':'Password',
             'maxlength': '50',
             'minlength':'8'
        })

        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name': 'password2',
            'type':'password',
            'class':'form-control',
             'placeholder':'Password',
             'maxlength': '50',
             'minlength':'8'
        })
   
   

    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name','username','email','password1', 'password2']
        
        def clean_username(self):
            username = self.cleaned_data.get('username')

        # Check if the username is already taken
            if CustomUser.objects.filter(username=username).exists():
                raise forms.ValidationError('This username is already taken.')

        # Check if the username is empty
            if not username:
                raise forms.ValidationError('Please enter a username.')

            return username

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image','username','first_name','last_name', 'email', 'mobile_Number']


class AdminProfileForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile_Number', 'image']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields ='__all__'

class DoctorEditProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields =['first_name','last_name','mobile_Number','email']

# class PatientEditProfileForm
class PatientEditProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name','last_name','mobile_Number','email','cpr','dof','blood','height','weight','sensitivity']

class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = appointment
        # fields = ['department', 'doctor', 'day', 'time']
        fields = ['day', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'placeholder': 'Day',
            'class':'form-control',
        })
        self.fields['time'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'placeholder': 'Time',
            'class':'form-control',
        })