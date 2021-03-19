# Generated by Django 3.0.5 on 2020-05-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tac', '0006_auto_20200514_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='tac_detail',
            name='bigbook_bg_image',
            field=models.ImageField(default=None, upload_to='img/tac', null= True),
        ),
        migrations.AddField(
            model_name='tac_detail',
            name='inventory_bg_image',
            field=models.ImageField(default=None, upload_to='img/tac', null= True),
        ),
        migrations.AddField(
            model_name='tac_detail',
            name='logo',
            field=models.ImageField(default=None, upload_to='img/tac', null= True),
        ),
        migrations.AddField(
            model_name='tac_detail',
            name='logo_black',
            field=models.ImageField(default=None, upload_to='img/tac', null= True),
        ),
        migrations.AddField(
            model_name='tac_detail',
            name='project_image',
            field=models.ImageField(default=None, upload_to='img/tac', null= True),
        ),
    ]