from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group, auth, Permission
from django.contrib import messages
from django.http import HttpResponse
from app.forms import RegisterForm, Profileform
from django.contrib.auth import authenticate, login
from app.models import Items, Items_List, Profile

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
                        direction =request.POST['direction'],
                        item_type =request.POST['item_type'],)
            current_user = request.user.id
            item.save()
            name = item.id
            add_author(request,current_user,name)
        else:
            pass
        return redirect('/items/')
    else:
        form = Profileform()
        current_user = request.user.id
        items = Items_List.objects.all().select_related('item_list').filter(user_name_id = current_user).order_by('item_list__item_name')
        lists = Items_List.objects.select_related('item_list')
        return render(request,'author_items.html',{'items':items,'form':form})

def add_author(request,current_user,name):
    assigndata = Items_List(
        user_name_id = current_user,
        item_list_id = name,
    )
    assigndata.save()

def edititems(request, id):
    if request.method == 'POST':
        item = Items_List.objects.get(item_list_id = id)
        item.item_list.author = request.POST['author']
        # item.item_list.profile_pic = request.FILES['profile_pic']
        item.item_list.item_name = request.POST['item_name']
        item.item_list.servings = request.POST['servings']
        item.item_list.preparation_time = request.POST['preparation_time']
        item.item_list.cooking_time = request.POST['cooking_time']
        # item.item_list.food_image = request.FILES['food_image']
        item.item_list.ingredients = request.POST['ingredients']
        item.item_list.direction = request.POST['direction']
        item.item_list.item_type = request.POST['item_type']
        item.item_list.save()
        return redirect('/items/')
    else:
        return redirect('/items/')

def recipe(request):
    items = Items.objects.all().order_by('item_name')
    return render(request,'recipe.html',{'items':items})

def viewrecipe(request,id):
    item = Items.objects.get(id=id)
    return render(request,'viewrecipe.html',{'item':item})

def authors_page(request,id):
    item = Items.objects.get(id = id)
    auth = Items.objects.values_list('author',flat=True).get(id = id)
    pages = Items.objects.all().filter(author=auth)
    count = pages.count()
    return render(request,'authors_page.html',{'auth':auth,'pages':pages,'item':item,'count':count})

def addprofile(request):
    if request.method == 'POST':
        item = Items(author=request.POST['author'],
                    profile_pic=request.FILES['profile_pic'],
                    item_name=request.POST['item_name'],
                    servings =request.POST['servings'],
                    preparation_time =request.POST['preparation_time'],
                    cooking_time =request.POST['cooking_time'],
                    food_image =request.FILES['food_image'],
                    ingredients =request.POST['ingredients'],
                    direction =request.POST['direction'],
                    item_type =request.POST['item_type'],)
        current_user = request.user.id
        item.save()
        return redirect('/items/')
    else:
        return redirect('/items/')

def editprofile(request, id):
    if request.method == 'POST':
        item = Items_List.objects.get(item_list_id = id)
        item.item_list.author = request.POST['author']
        item.item_list.item_name = request.POST['item_name']
        item.item_list.servings = request.POST['servings']
        return redirect('/items/')
    else:
        return redirect('/items/')

def logout(request):
    auth.logout(request)
    return redirect('app:home')

