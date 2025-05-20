from django import forms 
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class StudentForm(forms.ModelForm):
    class Meta: 
        model =Student
        fields ="__all__"
class RegisterForm(UserCreationForm):
    class Meta :
        model=User
        fields=['username','first_name','last_name','email']
class changedata(UserChangeForm):
    password=None
    class Meta :
        model=User
        fields=['username','first_name','last_name','email']