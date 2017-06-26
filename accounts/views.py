# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def home(request):
    numbers = [1,2,3,4,5]
    name = "Sarbjit Singh"
    args = {'myname' : name, 'numbers':numbers}
    return render(request,'accounts/home.html',args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()
    args = {'form' : form}
    return render(request,'accounts/reg_form.html',args)

#@login_required
def view_profile(request):
    args = {'user' : request.user}
    return render(request,'accounts/profile.html',args)

# From documentation regarding instance keyword
# A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied,
# save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model:

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
    args = {'form' : form}
    return render(request,'accounts/edit_profile.html',args)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form' : form}
    return render(request,'accounts/change_password.html',args)
