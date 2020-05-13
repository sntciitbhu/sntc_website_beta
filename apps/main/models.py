from django.db import models
from django.conf import settings
from apps.forms.models import Form
from datetime import datetime
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )
    signup_form = models.ForeignKey(Form, on_delete = models.SET_DEFAULT, related_name = "signup_form", default = None, blank=True,help_text="The Registraion details to be asked during SignUp" )
    extra_profile_form = models.ForeignKey(Form, on_delete = models.SET_DEFAULT,related_name = "extra_fields", default = None, blank=True,help_text="The Extra profile details other than the Sign_up to show in dashboard profile section" )

    def __str__(self):
        return "User Profile"