# Generated by Django 4.2.7 on 2023-11-20 01:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todosite", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="profile_picture",
        ),
    ]
