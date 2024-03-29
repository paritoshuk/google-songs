# Generated by Django 2.2.3 on 2019-07-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_link', models.CharField(max_length=200)),
                ('output_link', models.CharField(max_length=200)),
                ('ranking', models.IntegerField(default=0)),
                ('user_played', models.BooleanField()),
            ],
        ),
    ]
