from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# It will inherit the built in form i.e UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserform(UserCreationForm):  
    class Meta:
        model: User
        feilds = ['username' , 'first_name' , 'last_name' , 'email']

