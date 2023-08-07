from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.core.validators import integer_validator


class UserAccount(models.Model):

    username = models.CharField(max_length=25, null=True, blank=True)
    account_no = models.CharField(max_length=25, unique=True, null=True, validators=[integer_validator])
    token = models.CharField(max_length=40, blank=True, null=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now, blank=True, null=True)
    access_datetime = models.DateTimeField('date accessed', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'account_no'

    def update_access_datetime(self):
        # 最終アクセス日時を現在日時で更新
        update = UserAccount.objects.get(account_no=self.account_no)
        update.access_datetime = timezone.now()
        update.save()

    def __str__(self):
        dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
        if self.username is not None and self.account_no is not None:
            return 'アカウント番号：' + str(self.account_no) + '　' + self.username + '　' + '最終アクセス：(' + dt + ')'
        elif self.username is not None:
            return str(self.username) + ' ' + '最終アクセス：(' + dt + ')'
        elif self.account_no is not None:
            return 'アカウント番号：' + str(self.account_no) + '　' + '最終アクセス：(' + dt + ')'
