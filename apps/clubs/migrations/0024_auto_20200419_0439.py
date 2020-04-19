# Generated by Django 3.0.5 on 2020-04-19 04:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0023_auto_20200418_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aero_head',
            name='added_by',
        ),
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 910676), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='aero_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 910654), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 913178), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='astro_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 913160), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 925888), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='biz_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 925865), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 931161), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='cops_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 931142), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 928555), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='csi_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 928536), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 933807), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='robo_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 933786), verbose_name='date of registration'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_close',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 936441), verbose_name='date of registration close'),
        ),
        migrations.AlterField(
            model_name='sae_event',
            name='date_registration_open',
            field=models.DateTimeField(null=datetime.datetime(2020, 4, 19, 4, 39, 43, 936422), verbose_name='date of registration'),
        ),
        migrations.CreateModel(
            name='club_head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('club_id', models.CharField(default='null', max_length=50)),
                ('about', models.TextField()),
                ('tagline', models.CharField(default='null', max_length=100)),
                ('quote', models.CharField(default='null', max_length=100)),
                ('logo_img', models.ImageField(default='null', upload_to='upload/img/aero')),
                ('facebook', models.URLField(default='null', max_length=500)),
                ('twitter', models.URLField(default='null', max_length=500)),
                ('insta', models.URLField(default='null', max_length=500)),
                ('git', models.URLField(default='null', max_length=500)),
                ('linkedin', models.URLField(default='null', max_length=500)),
                ('youtube', models.URLField(default='null', max_length=500)),
                ('club_room_location', models.CharField(default='null', max_length=50)),
                ('contact', models.CharField(default='null', max_length=50)),
                ('email', models.CharField(default='null', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
