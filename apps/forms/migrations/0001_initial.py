# Generated by Django 3.0.5 on 2020-05-07 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Text Small', 'text'), ('Date', 'date'), ('E-mail', 'email'), ('Number', 'number'), ('Link', 'url'), ('Text Large', 'textarea')], max_length=50)),
                ('name', models.CharField(default=None, max_length=50)),
                ('default_value', models.CharField(blank=True, default=None, max_length=500)),
                ('placeholder_value', models.CharField(default=None, max_length=500)),
                ('required', models.BooleanField(default=True)),
                ('readOnly', models.BooleanField(default=True)),
                ('Validation_Error', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('value', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UploadField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Image', 'image'), ('File', 'file')], max_length=50)),
                ('name', models.CharField(default=None, max_length=50)),
                ('placeholder_value', models.CharField(default=None, max_length=500)),
                ('required', models.BooleanField(default=True)),
                ('readOnly', models.BooleanField(default=True)),
                ('uploadTo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SelectionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Drop Down', 'text'), ('Single Option', 'radio'), ('Multiple Option', 'checkbox')], max_length=50)),
                ('name', models.CharField(default=None, max_length=50)),
                ('placeholder_value', models.CharField(default=None, max_length=500)),
                ('required', models.BooleanField(default=True)),
                ('readOnly', models.BooleanField(default=True)),
                ('options', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forms.Option')),
            ],
        ),
    ]