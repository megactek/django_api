# Generated by Django 4.1.2 on 2022-10-11 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='author',
        ),
    ]
