# Generated by Django 2.0.5 on 2018-07-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumy', '0003_auto_20180711_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrumyStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.CharField(max_length=25, verbose_name='User name')),
            ],
            options={
                'verbose_name_plural': 'Scrumy Story',
            },
        ),
    ]