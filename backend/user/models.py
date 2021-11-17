from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=9)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    visit_time = models.IntegerField(default=0)
    adress = models.CharField(max_length=50, null=True, blank=True)
