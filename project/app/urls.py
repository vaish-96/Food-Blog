from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('items/', views.items, name='items'),
    path('logout/', views.logout, name='logout'),
]