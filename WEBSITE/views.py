from django.shortcuts import render, redirect
from django.http import HttpResponse

def Base(request):

   return render(request,'base.html')

def Login(request):

    return render(request,'login.html')

def Register(request):

    return render(request,'register.html')

def Landing(request):

    return render(request, 'landing.html')

def Woi(request):

    return render(request, 'woi.html')