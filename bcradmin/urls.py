from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('administrator/', views.admin_home, name='adminHomepage'),
    path('checking/',views.check_application,name='checkApplication'),
    path('manageroom/',views.manage_room,name='manageroom'),
    path('manageuser',views.manage_user,name='manageuser'),
    path('storage/',views.manage_storage,name='managestorge'),
    path('checking/edit/<int:id>',views.check_application_edit,name='checkApplicationEdit'),
]
