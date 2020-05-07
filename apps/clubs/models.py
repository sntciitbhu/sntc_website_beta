from django.db import models
from django.conf import settings
from apps.forms.models import Form

from datetime import datetime
from django.contrib.auth.models import User



class details(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )

    # About the Club
    name = models.CharField(max_length=50, default = None)
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = None)
    quote = models.CharField(max_length=100, default = None)
    logo_img = models.ImageField(upload_to='upload/img/', default = None)


    # Club external Links
    facebook = models.URLField(max_length=500, default= None, blank=True)
    twitter = models.URLField(max_length=500, default= None, blank=True) 
    insta = models.URLField(max_length=500, default= None, blank=True)
    git = models.URLField(max_length=500, default= None, blank=True)
    linkedin = models.URLField(max_length=500, default= None, blank=True)
    youtube = models.URLField(max_length=500, default= None, blank=True)

    # Club contact details
    club_room_location = models.CharField(max_length=50, default = None)
    contact = models.CharField(max_length=50, default = None)
    email = models.CharField(max_length=50, default = None)

    # Club Images for About


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "details"

class about_images(models.Model):
    club_name = models.ForeignKey(details, on_delete = models.CASCADE, default = None, blank=True, related_name = "about_images" )


    photo = models.ImageField(upload_to='img/about', default = 'null')
    def __str__(self):
        return "photo"

    class Meta:
        verbose_name_plural = "about_images"


class highlights(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )

    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "highlights"

class events(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',auto_now_add=True)
    date_registration_close = models.DateTimeField('date of registration close',auto_now_add=True)
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_form = models.ForeignKey(Form, on_delete = models.SET_DEFAULT, default = None, blank=True )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "events"

class workshops(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    registration_form = models.OneToOneField(Form, on_delete = models.SET_DEFAULT, default = None, blank=True )

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "workshops"
