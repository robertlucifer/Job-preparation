from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username'] # the user name here reference the name entered in the input field.
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged In")
            return redirect('home')
        else:
            messages.success(request,"Oops something went wrong..!")
            return redirect('home')
    else:

        return render(request,'home.html',{})

def logout_user(request):
    pass


