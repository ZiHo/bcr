from django.shortcuts import render

def index(request):
    response = render(request,'login.html')
    return response