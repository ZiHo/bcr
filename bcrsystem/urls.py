from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('homepage/', views.homeFunction, name='homepage'),
    path('logout/', views.user_logout, name='user_logout'),
    path('booking/', views.bookClassroom, name='book_classroom'),
    path('canceling/', views.cancelClassroom, name='cancel_classroom'),
    path('longbooking/', views.loogbookClassroom, name='longbook_classroom'),
    path('feedback/', views.useFeedback, name='use_feedback'),
    path('mailbox/', views.mailbox, name='mailbox'),
    path('myprofile/', views.myProfile, name='myProfile'),
    path('result/', views.showResult, name='showResult'),
    path('cancelresult/', views.canceling, name='canceling'),
    path('feedback/edit/<int:id>', views.feedbackEdit, name='feedbackEdit'),
]
