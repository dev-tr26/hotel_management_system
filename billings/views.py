
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def billing_home(request):
    return HttpResponse("Welcome to the Billing Section")
