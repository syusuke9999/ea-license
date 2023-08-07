# Generated by Django 4.2.4 on 2023-08-07 19:24

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, null=True)),
                ('account_no', models.CharField(max_length=25, null=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.')])),
                ('token', models.CharField(max_length=40, null=True)),
                ('access_datetime', models.DateTimeField()),
            ],
        ),
    ]
