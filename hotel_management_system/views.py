from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("          connected db to msql , Welcome to the Hotel Management System!!!         ")

