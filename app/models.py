from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
	name = models.SlugField()
	title = models.CharField(max_length=50)
	intro = models.TextField()
	content = models.TextField()
	image = models.ImageField(upload_to="adminimages")
	
	def __unicode__(self):
		return self.title
		

class MenuItem(models.Model):
	title = models.CharField(max_length=10)
	destination = models.CharField(max_length=255)
	position = models.IntegerField(unique=True)
	
	def __unicode__(self):
		return self.title		

class Review(models.Model):
	content = models.TextField()
	
	def __unicode__(self):
		return self.content
		
	

	