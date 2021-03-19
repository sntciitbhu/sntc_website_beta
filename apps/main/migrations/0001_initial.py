# Generated by Django 3.0.5 on 2020-05-11 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0002_auto_20200511_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_profile_form', models.ForeignKey(blank=True, default=None, help_text='The Extra profile details other than the Sign_up to show in dashboard profile section', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='extra_fields', to='forms.Form')),
                ('signup_form', models.ForeignKey(blank=True, default=None, help_text='The Registraion details to be asked during SignUp', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='signup_form', to='forms.Form')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]