# Generated by Django 2.2.3 on 2019-07-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='time_stamp',
            field=models.CharField(default='test', max_length=200),
        ),
    ]
