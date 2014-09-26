from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Camp(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class CampUser(models.Model):
    camp = models.ForeignKey(Camp)
    user = models.ForeignKey(User)


class Activity(models.Model):
    name = models.CharField(max_length=500)
    supervisor = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField()
    start_date = models.DateTimeField('Start Date', default=datetime.now())
    end_date = models.DateTimeField('End Date', default=datetime.now())


class Action(models.Model):
    activity = models.ForeignKey(Activity)
    user = models.ForeignKey(User)
    status = models.BooleanField(default=False)
    comment = models.CharField(max_length=1000)
    updated_at = models.DateTimeField('Updated At')


class ActionHistory(models.Model):
    activity = models.ForeignKey(Activity)
    user = models.ForeignKey(User)
    status = models.BooleanField(default=False)
    comment = models.CharField(max_length=1000)
    updated_at = models.DateTimeField('Updated At')