# Generated by Django 4.0.2 on 2022-02-08 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freeboard',
            fields=[
                ('b_no', models.AutoField(primary_key=True, serialize=False)),
                ('b_id', models.CharField(max_length=100)),
                ('b_title', models.CharField(max_length=1000)),
                ('b_content', models.TextField()),
                ('b_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 11, 17, 14, 917626))),
                ('b_hit', models.IntegerField(default=1)),
            ],
        ),
    ]
