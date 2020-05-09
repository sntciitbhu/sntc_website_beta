from django.db import models
from django.conf import settings
from apps.forms.models import Form

from datetime import datetime
from django.contrib.auth.models import User

from io import BytesIO
from PIL import Image
from django.core.files import File


def modify (image, size_x, size_y, file_type):
    im=Image.open(image)
    size = size_x,size_y
    im.thumbnail(size)
    im_io=BytesIO()
    if (file_type == "JPEG"):
        im= im.convert('RGB')
    im.save(im_io, file_type, quality=60)
    new_image = File(im_io,name=image.name)
    return new_image




class details(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, blank=True, null=True )

    # About the Club
    name = models.CharField(max_length=50, default = None)
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = None)
    quote = models.CharField(max_length=100, default = None)
    logo_img = models.ImageField(upload_to='img/', default = None, help_text = "Aspect Ratio 1:1 for best restuls")
    logo_img_black = models.ImageField(upload_to='img/', default = None,  help_text = "Aspect Ratio 2:1 for best restuls")


    # Other Images
    explore_bacground_img = models.ImageField(upload_to='img/', default = None,  help_text = "Aspect Ratio 7:3 for best restuls")
    workshop_img = models.ImageField(upload_to='img/', default = None,  help_text = "Aspect Ratio 9:16 for best restuls")



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

    def save(self, *args, **kwargs):
        self.logo_img = modify(self.logo_img,400,400,'PNG')
        self.logo_img_black = modify(self.logo_img_black,100,50,'PNG')
        self.explore_bacground_img = modify(self.explore_bacground_img,1400,600,'JPEG')
        self.workshop_img = modify(self.workshop_img,450,800,'JPEG')
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "details"

class about_images(models.Model):
    club_name = models.ForeignKey(details, on_delete = models.CASCADE, default = None, blank=True, related_name = "about_images" )


    photo = models.ImageField(upload_to='img/', default = 'null', help_text = "Aspect Ratio 4:3 for best restuls")
    def __str__(self):
        return "photo"

    def save(self, *args, **kwargs):

        self.photo = modify(self.photo,800,600,'logo_'+self.name,'JPEG')
        super().save(*args, **kwargs)

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
    image = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3 for best restuls")
    date_registration_open = models.DateTimeField('date of registration',auto_now_add=True)
    date_registration_close = models.DateTimeField('date of registration close',auto_now_add=True)
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= None, blank=True)
    ps_link = models.URLField(max_length=500, default= 'null', blank=True)
    registration_form = models.ForeignKey(Form, on_delete = models.SET_DEFAULT, default = None, blank=True,help_text="The Basic Profile Information will be taken automatically on registratoin. Cretate a form only for extra info needed. Select a blank form if you do not need any other Details" )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image = modify(self.image,600,450,'logo_'+self.name,'JPEG')
        super().save(*args, **kwargs)


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
