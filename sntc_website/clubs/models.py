from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class aero_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/aero', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
    
    
class aero_about_image(models.Model):
    photo = models.ImageField(upload_to='img/aero', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class aero_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class aero_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class aero_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name
      
      
      
      
      
      
class astro_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/astro', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
  
class astro_about_image(models.Model):
    photo = models.ImageField(upload_to='img/astro', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class astro_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class astro_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class astro_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name


      
      
      
      
      
      
      
      
            
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
class biz_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/biz', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
  
class biz_about_image(models.Model):
    photo = models.ImageField(upload_to='img/biz', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class biz_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class biz_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class biz_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name


      
      
      
class csi_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/csi', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
  
class csi_about_image(models.Model):
    photo = models.ImageField(upload_to='img/csi', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class csi_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class csi_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class csi_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name


      

      
      
      
      
class cops_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/cops', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
  
class cops_about_image(models.Model):
    photo = models.ImageField(upload_to='img/cops', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class cops_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class cops_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class cops_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name


  
      
      
class robo_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/robo', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
  
class robo_about_image(models.Model):
    photo = models.ImageField(upload_to='img/robo', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class robo_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class robo_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class robo_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name



      
class sae_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/sae', default = 'null')
    facebook = models.URLField(max_length=500, default= 'null')
    twitter = models.URLField(max_length=500, default= 'null')
    insta = models.URLField(max_length=500, default= 'null')
    git = models.URLField(max_length=500, default= 'null')
    linkedin = models.URLField(max_length=500, default= 'null')
    youtube = models.URLField(max_length=500, default= 'null')
    club_room_location = models.CharField(max_length=50, default = 'null')
    contact = models.CharField(max_length=50, default = 'null')
    email = models.CharField(max_length=50, default = 'null')
    
    def __str__(self):
        return self.name
  
class sae_about_image(models.Model):
    photo = models.ImageField(upload_to='img/sae', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class sae_highlight(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.name

class sae_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class sae_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    date_registration_open = models.DateTimeField('date of registration',null = datetime.now())
    date_registration_close = models.DateTimeField('date of registration close',null = datetime.now())
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name
