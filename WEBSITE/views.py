from django.shortcuts import render, redirect
from django.http import HttpResponse

def Base(request):

    return render(request,'base.html')