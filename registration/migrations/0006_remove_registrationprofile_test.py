# Generated by Django 2.0.12 on 2019-10-04 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_registrationprofile_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationprofile',
            name='test',
        ),
    ]
