from django.db import models
from django.contrib.auth.models import User


class classroom(models.Model):
    room_location = models.CharField(max_length=15)
    max_people = models.IntegerField(default=0)
    is_labroom = models.BooleanField(default=0)

    def __str__(self):
        return "%s" % self.room_location


class storageType(models.Model):
    type_description = models.TextField(null=True)

    def __str__(self):
        return "%s" % self.type_description


class storageInfo(models.Model):
    type_id = models.ForeignKey(storageType, on_delete=models.DO_NOTHING)
    storage_comment = models.TextField(null=True)


class borrowInfo(models.Model):
    classroom_id = models.ForeignKey(classroom, on_delete=models.DO_NOTHING)
    borrower_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    requirement = models.TextField(null=True)


class clean(models.Model):
    cleaner_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    classroom_id = models.ForeignKey(classroom, on_delete=models.DO_NOTHING)
    #clean_time = models.DateTimeField(auto_now_add=True)
    is_clean = models.BooleanField(default=False)


class credit(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    credit_num = models.IntegerField(default=0)


class creditRecord(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    in_decrease = models.BooleanField(default=False)
    balance = models.IntegerField(default=0)
    credit_time = models.DateTimeField(auto_now_add=True)
