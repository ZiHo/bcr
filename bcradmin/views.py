from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.urls import reverse


def user_logout(request):
    auth.logout(request)
    return redirect(reverse('user_login'))

@login_required(login_url='user_login')
def admin_home(request):
    return render(request, 'Admin_homepage.html')


@login_required(login_url='user_login')
def check_application(request):
    return render(request, 'Admin_CheckApplication.html')


@login_required(login_url='user_login')
def manage_room(request):
    return render(request, 'Admin_ManageRoom.html')


@login_required(login_url='user_login')
def manage_user(request):
    return render(request, 'Admin_MangeUser.html')


@login_required(login_url='user_login')
def manage_storage(request):
    return render(request, 'Admin_Storage.html')
