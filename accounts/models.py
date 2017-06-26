# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',blank=True)

    def __unicode__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

# Signals are used to run a command once an operation is performed
# In our case, when we create a new user, so far we have to create the user profile manually
# With signals, we are intercepting "create" and then creating user profile automatically
# FK = PK(id) of auth_user table for UserProfile

post_save.connect(create_profile,sender=User)

# TODO : Use formset for editing this along with profile
