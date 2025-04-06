from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, EmailAuthenticationForm

def guest_home(request):
    if not request.user.is_authenticated:
        return redirect('templates/guests/guest_login')
    return render(request, 'templates/base/home.html')  # Django renders this after login


def guest_login(request):
    if request.method == "POST":
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Sets session cookie
            messages.success(request, "LOGIN SUCCESSFUL!!")
            return redirect('customers:customer_home')
        else:
            messages.error(request, "Invalid Username or Password. Please try again.")
            return render(request, 'templates/auth/login.html', {'form': form})
    else:
         form = EmailAuthenticationForm()
    context = {'form': form}
    
    return render(request, 'templates/auth/login.html',context )



def guest_logout(request):
    logout(request)
    return redirect('customers:guest_login')



def guest_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('customers:customer_home')
        else:
            messages.error(request, "Registration failed - please check the form")
            return render(request, 'templates/auth/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    
    return render(request, 'templates/auth/register.html', context )