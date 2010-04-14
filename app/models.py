from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	dateModified = models.DateTimeField()
	text = models.TextField()
	publicationDate = models.DateTimeField()
	state_Choices = ((u'New', u'New'),(u'App',u'Approved'),(u'Exp',u'Expired'))
	
	def __unicode__(self):
		return self.title

	