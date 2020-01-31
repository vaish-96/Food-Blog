from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth, Permission
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def base(request):
    return render(request,'base.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user = User.objects.create_user('xyz')
        user.username = request.POST['username']
        user.email = request.POST['email']
        pword = request.POST['password']
        confirmword = request.POST['cpassword']
        user.is_staff = True
        if pword == confirmword:
            user.set_password(pword) 
            user.save()
            registered=True
        else:
            messages.error(request,'Password not matched')
    return render(request,'register.html',{'registered':registered})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return  redirect('app:items')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('app:login')
    else:
        return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def items(request):
    return render(request,'items.html')

def logout(request):
    auth.logout(request)
    return  redirect('app:home')

    # https://carlofontanos.com/creating-a-registration-page-in-django/