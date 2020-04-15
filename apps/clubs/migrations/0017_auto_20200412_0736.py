# Generated by Django 3.0.5 on 2020-04-12 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0016_auto_20200412_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 344434), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 344413), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 347773), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 347752), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 360507), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 360484), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 365825), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 365806), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 363202), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 363183), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 368482), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 368463), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 371124), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 12, 7, 36, 32, 371105), verbose_name='date of registration'),
        ),
    ]