# Generated by Django 3.0.5 on 2020-04-19 05:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0024_auto_20200419_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 575017), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 574995), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 577518), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 577497), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 590253), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 590231), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='club_head',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 595500), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 595481), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 592898), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 592878), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 598108), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 598088), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 600706), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 5, 2, 3, 600686), verbose_name='date of registration'),
        ),
    ]
