from django.db import models
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User

class Form(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Field(models.Model):
    fieldset = models.ForeignKey(Form, on_delete = models.CASCADE, default = None, blank=True,related_name = "fields" )
    type_choices = ( 
    ("text","Text Small"), 
    ( "date","Date"), 
    ( "email","E-mail"), 
    ( "number","Number"), 
    ( "url","Link"), 
    ( "textarea","Text Large"), 
    ("image", "Image"), 
    ("file", "File"),
    ("dropdown","Drop Down"), 
    ("radio","Single Option"), 
    ("checkbox","Multiple Option"), 
    ) 
    Serialno = models.PositiveIntegerField(null=True, blank=True)
    required = models.BooleanField(default=False)
    name = models.CharField(max_length=50, default = None)
    type = models.CharField(choices = type_choices,max_length=50)
    default_value = models.CharField(max_length=500, default = None, blank=True)
    readOnly = models.BooleanField(default=False)
    uploadToURL = models.URLField(blank = True, default = None)

    def __str__(self):
        return self.name


# class UploadField(models.Model):
#     Serialno = models.PositiveIntegerField(null=True, blank=True)

#     form = models.ForeignKey(Fieldsets, on_delete = models.CASCADE, default = None, blank=True,related_name = "uploadfields" )
#     type_choices = ( 
#     ("image", "Image"), 
#     ("file", "File"), 
#     ) 
#     type = models.CharField(choices = type_choices,max_length=50)
#     name = models.CharField(max_length=50, default = None)
#     placeholder_value =  models.CharField(max_length=500, default = None)
#     required= models.BooleanField(default=True)
#     def __str__(self):
#         return self.name

# class SelectionField(models.Model):
#     Serialno = models.PositiveIntegerField(null=True, blank=True)
#     form = models.ForeignKey(Fieldsets, on_delete = models.CASCADE, default = None, blank=True, related_name = "selectionfields" )
#     type_choices = ( 

#     ) 
#     type = models.CharField(choices = type_choices,max_length=50)
#     name = models.CharField(max_length=50, default = None)
#     placeholder_value =  models.CharField(max_length=500, default = None)
#     required= models.BooleanField(default=True)
#     def __str__(self):
#         return self.name

class Option(models.Model):
    name = models.CharField(max_length=50, default = None)
    options = models.ForeignKey(Field, blank = True, null= True, on_delete = models.CASCADE, default = None )

    def __str__(self):
        return self.name



    

