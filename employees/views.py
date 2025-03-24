
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def employee_home(request):
    return HttpResponse("Welcome to the Employee Section")
