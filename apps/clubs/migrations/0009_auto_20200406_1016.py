# Generated by Django 3.0.5 on 2020-04-06 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20200406_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 601691), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 601669), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 604311), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 604292), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 608297), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 608275), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 623823), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 623804), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 621165), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 621143), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 626466), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 626446), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 629071), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 6, 10, 16, 8, 629051), verbose_name='date of registration'),
        ),
    ]
