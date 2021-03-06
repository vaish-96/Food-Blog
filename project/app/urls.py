from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('items/', views.items, name='items'),
    path('edititems/<int:id>/', views.edititems, name='edititems'),
    path('recipe/', views.recipe, name='recipe'),
    path('viewrecipe/<int:id>/', views.viewrecipe, name='viewrecipe'),
    path('authpage/<int:id>/', views.authors_page, name='authpage'),
    path('logout/', views.logout, name='logout'),
]