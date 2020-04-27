# Generated by Django 3.0.5 on 2020-04-19 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0027_auto_20200419_1142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='astro_about_image',
        ),
        migrations.DeleteModel(
            name='astro_event',
        ),
        migrations.DeleteModel(
            name='astro_head',
        ),
        migrations.DeleteModel(
            name='astro_highlight',
        ),
        migrations.DeleteModel(
            name='astro_workshop',
        ),
        migrations.DeleteModel(
            name='biz_about_image',
        ),
        migrations.DeleteModel(
            name='biz_event',
        ),
        migrations.DeleteModel(
            name='biz_head',
        ),
        migrations.DeleteModel(
            name='biz_highlight',
        ),
        migrations.DeleteModel(
            name='biz_workshop',
        ),
        migrations.DeleteModel(
            name='cops_about_image',
        ),
        migrations.DeleteModel(
            name='cops_event',
        ),
        migrations.DeleteModel(
            name='cops_head',
        ),
        migrations.DeleteModel(
            name='cops_highlight',
        ),
        migrations.DeleteModel(
            name='cops_workshop',
        ),
        migrations.DeleteModel(
            name='csi_about_image',
        ),
        migrations.DeleteModel(
            name='csi_event',
        ),
        migrations.DeleteModel(
            name='csi_head',
        ),
        migrations.DeleteModel(
            name='csi_highlight',
        ),
        migrations.DeleteModel(
            name='csi_workshop',
        ),
        migrations.DeleteModel(
            name='robo_about_image',
        ),
        migrations.DeleteModel(
            name='robo_event',
        ),
        migrations.DeleteModel(
            name='robo_head',
        ),
        migrations.DeleteModel(
            name='robo_highlight',
        ),
        migrations.DeleteModel(
            name='robo_workshop',
        ),
        migrations.DeleteModel(
            name='sae_about_image',
        ),
        migrations.DeleteModel(
            name='sae_event',
        ),
        migrations.DeleteModel(
            name='sae_head',
        ),
        migrations.DeleteModel(
            name='sae_highlight',
        ),
        migrations.DeleteModel(
            name='sae_workshop',
        ),
        migrations.RemoveField(
            model_name='details',
            name='images',
        ),
        migrations.AlterField(
            model_name='events',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 12, 58, 38, 831881), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='events',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 12, 58, 38, 831859), verbose_name='date of registration'),
        ),
    ]