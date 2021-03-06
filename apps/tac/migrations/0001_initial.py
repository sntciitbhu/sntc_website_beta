# Generated by Django 3.0.5 on 2020-05-08 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='project_categories',
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
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tac.project_categories')),
            ],
        ),
        migrations.CreateModel(
            name='tac_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('about_tac', models.TextField()),
                ('tagline', models.CharField(default='null', max_length=100)),
                ('facebook_link', models.URLField(blank=True, max_length=500)),
                ('twitter_link', models.URLField(blank=True, max_length=500)),
                ('insta_link', models.URLField(blank=True, max_length=500)),
                ('git_link', models.URLField(blank=True, max_length=500)),
                ('linkedin_link', models.URLField(blank=True, max_length=500)),
                ('youtube_link', models.URLField(blank=True, max_length=500)),
                ('location_link', models.CharField(blank=True, default='null', max_length=50)),
                ('contact_number', models.CharField(blank=True, default='null', max_length=50)),
                ('email', models.CharField(blank=True, default='null', max_length=50)),
                ('guidelines', models.TextField(default='null')),
                ('about_facilites', models.TextField(default='null')),
                ('project_content', models.TextField()),
                ('propose_your_project_link', models.URLField(default='null', max_length=500)),
                ('bigbook_content', models.TextField()),
                ('technical_teams_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tac_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='null', upload_to='img/tac')),
            ],
        ),
        migrations.CreateModel(
            name='teams_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('image', models.ImageField(default='null', upload_to='upload/img/tac')),
                ('details', models.TextField()),
                ('competetion_aim', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='team_students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('contact', models.CharField(default='null', max_length=12)),
                ('team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='students', to='tac.teams_list', verbose_name='students')),
            ],
        ),
        migrations.CreateModel(
            name='project_students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
                ('contact', models.CharField(default='null', max_length=12)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='students', to='tac.project_list', verbose_name='students')),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=500)),
                ('item_id', models.CharField(default='null', max_length=10)),
                ('issue_allowed', models.BooleanField()),
                ('item_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tac.inventory_category', verbose_name='item_type')),
            ],
        ),
    ]
