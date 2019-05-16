from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, bookingForm
from .models import *
from django.contrib import auth
from django.urls import reverse


def index(request):
    return render(request, 'new_homepage.html')


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
    if request.method == 'POST':
        bookform = bookingForm(request.POST)
        if bookform.is_valid():
            # ----------------------------------
            # Get the data from the booking form
            # ----------------------------------
            # booker_id = request.user.id
            classroomType = bookform.cleaned_data['Type']
            bookDate = bookform.cleaned_data['Date']
            userID = request.session.get('_auth_user_id')
            classroomLocation = bookform.cleaned_data['classroom_location']
            classroomID = classroom.objects.get(room_location=classroomLocation).id
            startHour = bookform.cleaned_data['Start_Time']
            endHour = bookform.cleaned_data['End_Time']
            # ----------------------------------
            # Check the previous booking order
            # ----------------------------------
            if bookInfo.objects.filter(classroom_id=classroomID, start_hour=startHour):
                bookError = "This classroom has been booked."
                context = {}
                context['book_error'] = bookError
                return render(request, 'Booking_page.html', context)
                # return redirect(reverse('showResult'),context)
            else:
                bookInfo.objects.create(
                    booker_id_id=userID,
                    book_date=bookDate,
                    classroom_id_id=classroomID,
                    start_hour=startHour,
                    end_hour=endHour,
                )
                bookSuccess = "You have successfully booked this room"
                context = {}
                context['book_success'] = bookSuccess
                return render(request, 'Booking_page.html', context)

    else:
        bookform = bookingForm()

    context = dict()
    context['bookform'] = bookform
    return render(request, 'Booking_page.html', context)


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


@login_required(login_url='user_login')
def showResult(requset):
    return render(requset, 'book_result.html')
