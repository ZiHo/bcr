from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import auth
from django.urls import reverse


def user_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = login_form.cleaned_data['user']
                auth.login(request, user)
                if request.user.is_superuser:
                    return redirect(request.GET.get('from', reverse('adminHomepage')))
                else:
                    return redirect(request.GET.get('from', reverse('homepage')))
        else:
            login_form = LoginForm()
        context = {}
        context['login_form'] = login_form

        return render(request, 'login.html', context)


def user_logout(request):
    auth.logout(request)
    return redirect(reverse('user_login'))


@login_required(login_url='user_login')
def homeFunction(request):
    return render(request, 'Homepage.html')


@login_required(login_url='user_login')
def bookClassroom(request):
    return render(request, 'Booking_page.html')


@login_required(login_url='user_login')
def cancelClassroom(request):
    return render(request, 'Cancel_page.html')


@login_required(login_url='user_login')
def loogbookClassroom(request):
    return render(request, 'Longterm_page.html')


@login_required(login_url='user_login')
def useFeedback(request):
    return render(request, 'Feedback_page.html')


@login_required(login_url='user_login')
def mailbox(request):
    return render(request, 'Mailbox_page.html')


@login_required(login_url='user_login')
def myProfile(request):
    return render(request, 'Porfile_page.html')
