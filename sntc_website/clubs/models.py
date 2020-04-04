from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class aero_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    tagline = models.CharField(max_length=100, default = 'null')
    logo_img = models.ImageField(upload_to='upload/img/aero', default = 'null')

    def __str__(self):
        return self.name
    
    
class aero_about_image(models.Model):
    photo = models.ImageField(upload_to='img/aero', default = 'null')
    
    def __str__(self):
        return "photo"
    
    
class aero_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
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
    date_registration_open = models.DateTimeField('date of registration')
    date_registration_close = models.DateTimeField('date of workshop')
    teamsize = models.IntegerField('max Team size',default = 1)
    refrences_link = models.URLField(max_length=500, default= 'null')
    ps_link = models.URLField(max_length=500, default= 'null')
    registration_link = models.URLField(max_length=500, default= 'null')
    def __str__(self):
        return self.name

class aero_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

class astro_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()

class astro_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

class astro_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name

class astro_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class astro_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

    
    
class biz_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    def __str__(self):
        return self.name

class biz_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

class biz_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name

class biz_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class biz_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

    
class cops_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    def __str__(self):
        return self.name

class cops_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

class cops_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name

class cops_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class cops_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

    
class csi_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    def __str__(self):
        return self.name

class csi_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

class csi_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name

class csi_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class csi_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

    
class robo_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    def __str__(self):
        return self.name

class robo_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

class robo_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name

class robo_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class robo_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

    
    
class sae_head(models.Model):
    name = models.CharField(max_length=50, default = 'null')
    club_id = models.CharField(max_length=50, default = 'null')
    about = models.TextField()
    def __str__(self):
        return self.name

class sae_highlight(models.Model):

    name = models.CharField(max_length=50)
    details = models.TextField()
    published_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

class sae_workshop(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date of workshop')
    presentation = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name

class sae_event(models.Model):

    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField('date event')
    image = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class sae_calendar(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    def __str__(self):
        return self.name

    


    

    
    