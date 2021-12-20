from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=2083)
    location = models.CharField(max_length=255)
    who_can_friend_me = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    languages_known = models.CharField(max_length=255)
    dob = models.DateField(default=None, blank= True, null=True)
    about = models.CharField(max_length=2083, default=None, blank=True, null=True)