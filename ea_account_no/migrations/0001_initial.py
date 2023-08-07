# Generated by Django 4.2.4 on 2023-08-07 19:24

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=25, null=True)),
                ('account_no', models.CharField(max_length=25, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.')])),
                ('token', models.CharField(blank=True, max_length=40, null=True)),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date joined')),
                ('access_datetime', models.DateTimeField(blank=True, null=True, verbose_name='date accessed')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]