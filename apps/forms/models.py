from django.db import models
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User

class Form(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )
    name = models.CharField(max_length=50, default = None)
    def __str__(self):
        return self.name


class InputField(models.Model):
    form = models.ForeignKey(Form, on_delete = models.CASCADE, default = None, blank=True )
    type_choices = ( 
    ("Text Small", "text"), 
    ("Date", "date"), 
    ("E-mail", "email"), 
    ("Number", "number"), 
    ("Link", "url"), 
    ("Text Large", "textarea"), 
    ) 
    type = models.CharField(choices = type_choices,max_length=50)
    name = models.CharField(max_length=50, default = None)
    default_value = models.CharField(max_length=500, default = None, blank=True)
    placeholder_value =  models.CharField(max_length=500, default = None)
    required = models.BooleanField(default=False)
    readOnly = models.BooleanField(default=False)
    Validation_Error = models.CharField(max_length=100, default = None)
    def __str__(self):
        return self.name


class UploadField(models.Model):
    form = models.ForeignKey(Form, on_delete = models.CASCADE, default = None, blank=True )
    type_choices = ( 
    ("Image", "image"), 
    ("File", "file"), 
    ) 
    type = models.CharField(choices = type_choices,max_length=50)
    name = models.CharField(max_length=50, default = None)
    placeholder_value =  models.CharField(max_length=500, default = None)
    required= models.BooleanField(default=True)
    uploadToURL = models.URLField()
    def __str__(self):
        return self.name

class SelectionField(models.Model):
    form = models.ForeignKey(Form, on_delete = models.CASCADE, default = None, blank=True )
    type_choices = ( 
    ("Drop Down", "text"), 
    ("Single Option", "radio"), 
    ("Multiple Option", "checkbox"), 
    ) 
    type = models.CharField(choices = type_choices,max_length=50)
    name = models.CharField(max_length=50, default = None)
    placeholder_value =  models.CharField(max_length=500, default = None)
    required= models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(max_length=50, default = None)
    value = models.CharField(max_length=50, default = None)
    options = models.ForeignKey(SelectionField, on_delete = models.CASCADE, default = None )

    def __str__(self):
        return self.name



    

