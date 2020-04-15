# Generated by Django 3.0.5 on 2020-04-12 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0018_auto_20200412_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 770963), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 770925), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 774214), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 774193), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 786768), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 786745), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 792383), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 792347), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 789477), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 789459), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 795265), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 795244), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 797901), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 13, 32, 50, 797883), verbose_name='date of registration'),
        ),
    ]