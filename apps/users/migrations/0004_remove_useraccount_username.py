# Generated by Django 4.2.5 on 2023-10-30 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_useraccount_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
    ]