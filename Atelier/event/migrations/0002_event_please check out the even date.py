# Generated by Django 4.1.6 on 2023-02-03 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 2, 3, 16, 39, 35, 677210))), name='please check out the even date'),
        ),
    ]