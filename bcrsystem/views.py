from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
            if creditrecord.objects.filter(classroom_id=classroomID, start_hour=startHour):
                bookError = "This classroom has been booked."
                context = {}
                context['book_error'] = bookError
                return render(request, 'Booking_page.html', context)
                # return redirect(reverse('showResult'),context)
            else:
                creditrecord.objects.create(
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

    context = {}
    context['bookform'] = bookform
    return render(request, 'Booking_page.html', context)


@login_required(login_url='user_login')
def cancelClassroom(request):
    userID = request.session.get('_auth_user_id')
    all_recordings = bookInfo.objects.filter(booker_id_id=userID)
    paginator = Paginator(all_recordings, 6)
    page_num = request.GET.get('page', 1)
    page_of_recordings = paginator.get_page(page_num)

    current_page_num = page_of_recordings.number  # 获取当前页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    ###
    classroom_Location = classroom.objects.all()
    context = {}
    context['classroom_location'] = classroom_Location
    context['page_range'] = page_range
    context['BookInfo_all_list'] = page_of_recordings
    return render(request, 'Cancel_page.html', context)


@login_required(login_url='user_login')
def canceling(request):
    if request.method == 'POST':
        id = request.POST['id']
        creditrecord.objects.filter(id=id).update(is_cancel=True)
        return redirect(request.GET.get('from', reverse('cancel_classroom')))
    else:
        return redirect('cancel_classroom')


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
    userID = request.session.get('_auth_user_id')
    changing_user = User.objects.all()
    user_credit = credit.objects.get(user_id_id=userID)
    all_recordings = creditRecord.objects.filter(user_id_id=userID)
    paginator = Paginator(all_recordings, 3)
    page_num = request.GET.get('page', 1)
    page_of_recordings = paginator.get_page(page_num)

    current_page_num = page_of_recordings.number  # 获取当前页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    ###
    context = {}
    context['page_range'] = page_range
    context['creditrecord_all_list'] = page_of_recordings
    return render(request, 'Porfile_page.html', context)


@login_required(login_url='user_login')
def showResult(requset):
    return render(requset, 'book_result.html')
