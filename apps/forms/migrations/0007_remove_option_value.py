# Generated by Django 3.0.5 on 2020-05-12 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20200512_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='value',
        ),
    ]
