from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.urls import reverse
from bcrsystem.models import *
from .forms import BookInfoEditAdminForm,ClassroomEditAdminForm,UserEditAdminForm
from django.contrib.auth.models import User


def user_logout(request):
    auth.logout(request)
    return redirect(reverse('user_login'))

@login_required(login_url='user_login')
def admin_home(request):
    if request.user.is_superuser:
        return render(request, 'Admin_homepage.html')
    else:
        raise Http404

@login_required(login_url='user_login')
def check_application(request):
    all_recordings = bookInfo.objects.all()
    paginator = Paginator(all_recordings, 6)
    page_num = request.GET.get('page', 1)
    page_of_recordings = paginator.get_page(page_num)
    current_page_num = page_of_recordings.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = dict()
    context['page_range'] = page_range
    context['BookInfo_all_list'] = page_of_recordings
    return render(request, 'Admin_CheckApplication.html', context)


@login_required(login_url='user_login')
def check_application_edit(request, id):
    if request.method == 'POST':
        changing_bookinfo = bookInfo.objects.get(pk=id)
        form = BookInfoEditAdminForm(data=request.POST, instance=changing_bookinfo)
        if form.is_valid():
            form.save()
            return redirect(reverse('checkApplication'))
        else:
            context = dict()
            context['form'] = form
            return render(request, 'Admin_CheckApplication_edit.html', context)
    else:
        classroom1 = get_object_or_404(bookInfo, pk=id)
        context = dict()
        context['form'] = BookInfoEditAdminForm(instance=classroom1)
        return render(request, 'Admin_CheckApplication_edit.html', context)


@login_required(login_url='user_login')
def manage_room(request):
    all_recordings = classroom.objects.all()
    paginator = Paginator(all_recordings, 10)
    page_num = request.GET.get('page', 1)
    page_of_recordings = paginator.get_page(page_num)
    current_page_num = page_of_recordings.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = dict()
    context['page_range'] = page_range
    context['classroom_all_list'] = page_of_recordings
    return render(request, 'Admin_ManageRoom.html',context)


@login_required(login_url='user_login')
def manage_room_edit(request,id):
    if request.method == 'POST':
        changing_classroom = classroom.objects.get(pk=id)
        form = ClassroomEditAdminForm(data=request.POST, instance=changing_classroom)
        if form.is_valid():
            form.save()
            return redirect(reverse('manageroom'))
        else:
            context = dict()
            context['form'] = form
            return render(request, 'Admin_ManageRoom_edit.html', context)
    else:
        bookInfo1 = get_object_or_404(bookInfo, pk=id)
        context = dict()
        context['form'] = ClassroomEditAdminForm(instance=bookInfo1)
        return render(request, 'Admin_ManageRoom_edit.html', context)


@login_required(login_url='user_login')
def manage_user(request):
    all_recordings = User.objects.all()
    paginator = Paginator(all_recordings, 4)
    page_num = request.GET.get('page', 1)
    page_of_recordings = paginator.get_page(page_num)
    current_page_num = page_of_recordings.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = dict()
    context['page_range'] = page_range
    context['user_all_list'] = page_of_recordings
    return render(request, 'Admin_MangeUser.html', context)


@login_required(login_url='user_login')
def manage_user_edit(request, id):
    if request.method == 'POST':
        changing_user = User.objects.get(pk=id)
        form = UserEditAdminForm(data=request.POST, instance=changing_user)
        if form.is_valid():
            form.save()
            return redirect(reverse('manageuser'))
        else:
            context = dict()
            context['form'] = form
            return render(request, 'Admin_ManageUser_edit.html', context)
    else:
        userInfo1 = get_object_or_404(User, pk=id)
        context = dict()
        context['form'] = UserEditAdminForm(instance=userInfo1)
        return render(request, 'Admin_ManageUser_edit.html', context)


@login_required(login_url='user_login')
def manage_storage(request):
    all_recordings = storageInfo.objects.all()
    paginator = Paginator(all_recordings, 8)
    page_num = request.GET.get('page', 1)
    page_of_recordings = paginator.get_page(page_num)

    current_page_num = page_of_recordings.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    context['page_range'] = page_range
    context['Storage_all_list'] = page_of_recordings
    return render(request, 'Admin_Storage.html',context)
