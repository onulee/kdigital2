# Generated by Django 4.0.2 on 2022-02-11 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_alter_member_u_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='u_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 11, 16, 9, 39, 686686)),
        ),
    ]