from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import UserToken


class EaAuthentication(admin.ModelAdmin):
    fields = ['username', 'account_no', 'token', 'access_datetime', ]


admin.site.register(UserToken, EaAuthentication)
admin.site.unregister(Group)
