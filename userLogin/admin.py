from django.contrib import admin
from .models import userInfo

@admin.register(userInfo)
class userInfoAdmin(admin.ModelAdmin):
    list_display = ('name','passwd')




# Register your models here.
