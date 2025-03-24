
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def order_home(request):
    return HttpResponse("Welcome to the Orders Section")
