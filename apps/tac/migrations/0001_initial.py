# Generated by Django 3.0.5 on 2020-04-10 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bigbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('item_id', models.CharField(default='null', max_length=100)),
                ('issue_allowed', models.BooleanField()),
                ('total_count', models.PositiveIntegerField()),
                ('min_reserve', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='guidelines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guideline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='inventory_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='project_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('image', models.ImageField(default='null', upload_to='upload/img/tac')),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('propose_your_project', models.URLField(default='null', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='tac_head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
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
                ('location', models.CharField(default='null', max_length=50)),
                ('contact', models.CharField(default='null', max_length=50)),
                ('email', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tac_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='null', upload_to='img/aero')),
            ],
        ),
        migrations.CreateModel(
            name='teams_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('image', models.ImageField(default='null', upload_to='upload/img/tac')),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='techteams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='team_students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('contact', models.CharField(default='null', max_length=12)),
                ('team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tac.teams_list', verbose_name='students')),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('contact', models.CharField(default='null', max_length=12)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tac.project_list', verbose_name='students')),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tac.project_list', verbose_name='students')),
            ],
        ),
    ]
