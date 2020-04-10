from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class tac_head(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	about = models.TextField()
	tagline = models.CharField(max_length=100, default = 'null')
	quote = models.CharField(max_length=100, default = 'null')
	logo_img = models.ImageField(upload_to='upload/img/aero', default = 'null')
	facebook = models.URLField(max_length=500, default= 'null',blank=True)
	twitter = models.URLField(max_length=500, default= 'null',blank=True)
	insta = models.URLField(max_length=500, default= 'null',blank=True)
	git = models.URLField(max_length=500, default= 'null',blank=True)
	linkedin = models.URLField(max_length=500, default= 'null',blank=True)
	youtube = models.URLField(max_length=500, default= 'null',blank=True)
	location = models.CharField(max_length=50, default = 'null')
	contact = models.CharField(max_length=50, default = 'null',blank=True)
	email = models.CharField(max_length=50, default = 'null',blank=True)

	def __str__(self):
		return self.name
      
class tac_image(models.Model):
	photo = models.ImageField(upload_to='img/aero', default = 'null')

	def __str__(self):
		return "photo"

    
class guidelines(models.Model):
	guideline = models.TextField()

	def __str__(self):
		return "guidelines"

      
class facilities(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	item_id = models.CharField(max_length=100, default = 'null')
	issue_allowed = models.BooleanField()
	#item_type = ()
	total_count = models.PositiveIntegerField()
	min_reserve = models.PositiveIntegerField()

	def __str__(self):
		return self.name
      
      

	
class project_list(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	category = 1
	image = models.ImageField(upload_to='upload/img/tac', default = 'null')
	details = models.TextField()

	def __str__(self):
		return self.name

class teams_list(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	student_details = 1
	category = 1
	image = models.ImageField(upload_to='upload/img/tac', default = 'null')
	details = models.TextField()

	def __str__(self):
		return self.name


      
class projects(models.Model):
  
	details = models.TextField()
	propose_your_project = models.URLField(max_length=500, default= 'null')

	def __str__(self):
		return "projects"

        
class bigbook(models.Model):
    details = models.TextField()
    
    def __str__(self):
        return "bigbook"
      

class techteams(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return "guidelines"
	

class categories(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	project = models.ForeignKey(project_list,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT)

	def __str__(self):
		return self.name
	
	
class inventory_category(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	
	def __str__(self):
		return self.name
	

class students(models.Model):
	project = models.ForeignKey(project_list,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=50, default = 'null')
	contact = models.CharField(max_length=12, default = 'null')
	
	def __str__(self):
		return self.name
	
	
class team_students(models.Model):
	team = models.ForeignKey(teams_list,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=50, default = 'null')
	contact = models.CharField(max_length=12, default = 'null')
	
	def __str__(self):
		return self.name

	

  
  
  
 
      