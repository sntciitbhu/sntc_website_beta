# Generated by Django 3.0.5 on 2020-05-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_remove_option_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='Validation_Error',
        ),
        migrations.RemoveField(
            model_name='field',
            name='placeholder_value',
        ),
        migrations.AlterField(
            model_name='fieldset',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
