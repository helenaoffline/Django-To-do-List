# Generated by Django 4.2.7 on 2023-11-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todosite", "0003_todogroup_newtodo"),
    ]

    operations = [
        migrations.AddField(
            model_name="newtodo",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
