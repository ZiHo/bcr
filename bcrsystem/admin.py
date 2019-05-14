from django.contrib import admin
from .models import classroom, storageType, storageInfo, borrowInfo, clean, credit, creditRecord


@admin.register(classroom)
class classroomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_location', 'max_people', 'is_labroom')


@admin.register(storageType)
class storageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_description')


@admin.register(storageInfo)
class storageInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_id', 'storage_comment')


@admin.register(borrowInfo)
class borrowInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'classroom_id', 'borrower_id', 'start_time', 'end_time', 'requirement')


@admin.register(clean)
class cleanAdmin(admin.ModelAdmin):
    list_display = ('cleaner_id', 'classroom_id', 'is_clean')


@admin.register(credit)
class creditAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'credit_num')


@admin.register(creditRecord)
class creditRecord(admin.ModelAdmin):
    list_display = ('user_id', 'in_decrease', 'balance', 'credit_time')
