from django.urls import path
from . import views 

urlpatterns = [
    path('', views.guest_home, name='home_page'),
    path('register/', views.guest_register, name='register'),
    path('login/', views.guest_login, name='login'),
    path('logout/', views.guest_logout, name='guest_logout'),
]
