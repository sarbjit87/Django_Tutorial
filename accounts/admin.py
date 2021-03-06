# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
admin.site.register(UserProfile)
#admin.site.site_header = 'Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info','city','website','phone')

    def user_info(self,obj):
        return obj.description

    def get_queryset(self,request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by('phone')
        return queryset

    user_info.short_description = 'Info'
