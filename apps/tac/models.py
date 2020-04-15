from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class tac_detail(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	about_tac = models.TextField()
	tagline = models.CharField(max_length=100, default = 'null')
	facebook_link = models.URLField(max_length=500,blank=True)
	twitter_link = models.URLField(max_length=500,blank=True)
	insta_link = models.URLField(max_length=500,blank=True)
	git_link = models.URLField(max_length=500,blank=True)
	linkedin_link = models.URLField(max_length=500,blank=True)
	youtube_link = models.URLField(max_length=500,blank=True)
	location_link = models.CharField(max_length=50, default = 'null',blank=True)
	contact_number = models.CharField(max_length=50, default = 'null',blank=True)
	email = models.CharField(max_length=50, default = 'null',blank=True)
	guidelines = models.TextField(default="null")
	about_facilites = models.TextField(default="null")
	project_content = models.TextField()
	propose_your_project_link = models.URLField(max_length=500, default= 'null')
	bigbook_content = models.TextField()
	technical_teams_content = models.TextField()



	def __str__(self):
		return self.name
      
class tac_image(models.Model):
	photo = models.ImageField(upload_to='img/tac', default = 'null')

	def __str__(self):
		return "photo"

    
class inventory_category(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	
	def __str__(self):
		return self.name
      
class inventory(models.Model):
	name = models.CharField(max_length=500, default = 'null')
	item_id = models.CharField(max_length=10, default = 'null')
	issue_allowed = models.BooleanField()
	item_type = (models.ForeignKey(inventory_category,default=1, verbose_name="item_type", on_delete=models.SET_DEFAULT))

	def __str__(self):
		return self.name
      
	
class project_categories(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	
	def __str__(self):
		return self.name
	
class project_list(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	category = (models.ForeignKey(project_categories,on_delete=models.SET_NULL,null=True))
	image = models.ImageField(upload_to='upload/img/tac', default = 'null')
	details = models.TextField()
	
	def __str__(self):
		return self.name

	

	


class teams_list(models.Model):
	name = models.CharField(max_length=50, default = 'null')
	image = models.ImageField(upload_to='upload/img/tac', default = 'null')
	details = models.TextField()
	competetion_aim = models.CharField(max_length=50, default = 'null')

	def __str__(self):
		return self.name


      
  	

class project_students(models.Model):
	project = models.ForeignKey(project_list,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT,related_name='students')
	name = models.CharField(max_length=50, default = 'null')
	contact = models.CharField(max_length=12, default = 'null')
	
	def __str__(self):
		return self.name
	
	
class team_students(models.Model):
	team = models.ForeignKey(teams_list,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT,related_name='students')
	name = models.CharField(max_length=50, default = 'null')
	contact = models.CharField(max_length=12, default = 'null')
	
	def __str__(self):
		return self.name