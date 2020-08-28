from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def shop_template(request):
    return render(request,'index.html')

# View to display the product
def product_template(request):
    return render(request,'products.html')

# SignUpForm
def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created successfully')
    else:
        fm = UserCreationForm()
    return render(request , 'signup.html' , {'form':fm})

