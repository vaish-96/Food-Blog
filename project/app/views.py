from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth, Permission
from django.contrib import messages
from django.http import HttpResponse
from app.forms import RegisterForm, Profileform
from django.contrib.auth import authenticate, login
from app.models import Items
# Create your views here.
def base(request):
    return render(request,'base.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'register.html', {'form': form,'error_message': 'Username already exists.'})
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, 'register.html', {'form': form,'error_message': 'Email already exists.'})
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, 'register.html', {'form': form,'error_message': 'Passwords do not match.'})
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                auth.login(request, user)
                return redirect('app:login')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return  redirect('app:items')
        else:
            return render(request,'login.html',{'error_message': 'Invalid Username or Password'})
    else:
        return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def items(request):
    if request.method == "POST":
        form = Profileform(request.POST, request.FILES) 
        if form.is_valid():
            item = Items(author=request.POST['author'],
                        profile_pic=request.FILES['profile_pic'],
                        item_name=request.POST['item_name'],
                        servings =request.POST['servings'],
                        preparation_time =request.POST['preparation_time'],
                        cooking_time =request.POST['cooking_time'],
                        food_image =request.FILES['food_image'],
                        ingredients =request.POST['ingredients'],
                        direction =request.POST['direction'],)
            
            item.save()
        return redirect('/items/')
    else:
        form = Profileform()
        items = Items.objects.all()
        return render(request,'items.html',{'items':items,'form':form})

def edititems(request, id):
    if request.method == 'POST':
        item = Items.objects.get(id=id)
        item.author = request.POST['author']
        item.profile_pic = request.FILES['profile_pic']
        item.item_name = request.POST['item_name']
        item.servings = request.POST['servings']
        item.preparation_time = request.POST['preparation_time']
        item.cooking_time = request.POST['cooking_time']
        item.food_image = request.FILES['food_image']
        item.ingredients = request.POST['ingredients']
        item.direction = request.POST['direction']
        item.save()
        return redirect('/items/')
    else:
        return redirect('/items/')

def recipe(request):
    items = Items.objects.all()
    return render(request,'recipe.html',{'items':items})

def viewrecipe(request,id):
    item = Items.objects.get(id=id)
    return render(request,'viewrecipe.html',{'item':item})

def logout(request):
    auth.logout(request)
    return  redirect('app:home')

    # https://carlofontanos.com/creating-a-registration-page-in-django/