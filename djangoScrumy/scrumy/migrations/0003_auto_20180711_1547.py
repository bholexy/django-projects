# Generated by Django 2.0.5 on 2018-07-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumy', '0002_auto_20180711_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='First Name of User'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Last Name of User'),
        ),
    ]
