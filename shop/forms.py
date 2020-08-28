from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm

# It will inherit the built in form i.e UserCreationForm
class SignUpForm(UserCreationForm):  
    class Meta:
        model: User
        feilds = ['username' , 'first_name' , 'last_name' , 'email']

