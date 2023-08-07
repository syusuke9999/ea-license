from django.contrib import admin
from .models import UserAccount


class AccountNoAdmin(admin.ModelAdmin):
    fields = ['account_no', 'username', 'access_datetime', ]
    list_display = ('account_no', 'username', 'access_datetime',)
    search_fields = ('account_no', 'username',)


# Register your models here.
admin.site.register(UserAccount, AccountNoAdmin)
