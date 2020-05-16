from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



from io import BytesIO
from PIL import Image
from django.core.files import File


def modify (image, size_x, size_y, file_type, img_name):
    im=Image.open(image)
    size = size_x,size_y
    im.thumbnail(size)
    im_io=BytesIO()
    if (file_type == "JPEG"):
        im= im.convert('RGB')
    im.save(im_io, file_type, quality=60)
    new_image = File(im_io,name=img_name+image.name)
    return new_image

# Create your models here.

class tac_detail(models.Model):
	name = models.CharField(max_length=50, default = None)
	about_tac = models.TextField()
	tagline = models.CharField(max_length=100, default = None)
	logo = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 1:1 for best restuls", default = None)
	logo_black = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 2:1 for best restuls", default = None)

	facebook = models.URLField(max_length=500, default= None, blank=True)
	twitter = models.URLField(max_length=500, default= None, blank=True) 
	insta = models.URLField(max_length=500, default= None, blank=True)
	git = models.URLField(max_length=500, default= None, blank=True)
	linkedin = models.URLField(max_length=500, default= None, blank=True)
	youtube = models.URLField(max_length=500, default= None, blank=True)


	location = models.CharField(max_length=50, default = None,blank=True)
	contact_number = models.CharField(max_length=50, default = None,blank=True)
	email = models.CharField(max_length=50, default = None,blank=True)

	guidelines = models.TextField(default=None)
	about_facilites = models.TextField(default=None)
	inventory_bg_image = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3 for best restuls", default = None)


	project_content = models.TextField()
	project_image = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 3:4 for best restuls", default = None)

	bigbook_content = models.TextField()
	bigbook_bg_image = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3 for best restuls", default = None)
	technical_teams_content = models.TextField()

	def save(self, *args, **kwargs):
		self.logo = modify(self.logo,400,400,'PNG',"tac_logo_img_")
		self.logo_black = modify(self.logo_black,100,50,'PNG',"tac_logo_img_black_")
		self.inventory_bg_image = modify(self.inventory_bg_image,1500,1200,'JPEG',"tac_inventory_bg_image_")
		self.bigbook_bg_image = modify(self.bigbook_bg_image,1500,1200,'JPEG',"tac_bigbook_bg_image_")

		self.project_image = modify(self.project_image,600,800,'JPEG',"tac_project_image_")
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "details"

      
class tac_image(models.Model):
	photo = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3 for best restuls", default = None)

	def save(self, *args, **kwargs):

		self.photo = modify(self.photo,800,600,'tac_image_'+self.name,'JPEG')
		super().save(*args, **kwargs)

	def __str__(self):
		return "photo"
	
	class Meta:
		verbose_name_plural = "tac_images"

    
class inventory_category(models.Model):
	name = models.CharField(max_length=50, default = None)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "inventory_categories"
      
class inventory(models.Model):
	name = models.CharField(max_length=500, default = None)
	item_id = models.CharField(max_length=10, default = None)
	issue_allowed = models.BooleanField()
	item_type = models.ForeignKey(inventory_category,default=1, verbose_name="item_type", on_delete=models.SET_DEFAULT)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "inventory_items"
      
	
class project_category(models.Model):
	name = models.CharField(max_length=50, default = None)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "project_categories"

	
class project(models.Model):
	name = models.CharField(max_length=50, default = None)
	category = models.OneToOneField(project_category,on_delete=models.SET_NULL,null=True)
	image = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3 for best restuls", default = None)
	details = models.TextField()

	def save(self, *args, **kwargs):

		self.image = modify(self.image,800,600,'JPEG','project_'+self.name)
		super().save(*args, **kwargs)
	
	def __str__(self):
		return self.name


class project_student(models.Model):
	roles = ( 
		("Leader","Leader"), 
		( "Member","Member"), 
		) 
	project = models.ForeignKey(project,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT,related_name='students')
	name = models.CharField(max_length=50, default = None)
	contact = models.CharField(max_length=12, default = None)
	role = models.CharField(choices = roles,max_length=10)

	
	def __str__(self):
		return self.name



class team(models.Model):
	
	name = models.CharField(max_length=50, default = None)
	image = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3 for best restuls", default = None)
	details = models.TextField()
	competetion_aim = models.CharField(max_length=50, default = None)
	team_photo = models.ImageField(upload_to='img/', help_text = "Aspect Ratio 4:3W for best restuls", default = None)

	def save(self, *args, **kwargs):

		self.image = modify(self.image,800,600,'JPEG','team_'+self.name)
		self.team_photo = modify(self.team_photo,800,600,'JPEG','team_'+self.name)

		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

class team_student(models.Model):
	roles = ( 
		("Leader","Leader"), 
		( "Member","Member"), 
		( "Manager","Manager"), 
		) 

	team = models.ForeignKey(team,  default=1, verbose_name="students", on_delete=models.SET_DEFAULT,related_name='students')
	name = models.CharField(max_length=50, default = None)
	role = models.CharField(choices = roles,max_length=10)

	contact = models.CharField(max_length=12, default = None)

	
	def __str__(self):
		return self.name