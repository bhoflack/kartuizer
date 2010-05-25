"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from kartuizer.app.models import Page

class PageTest(TestCase):
	def test_pretty_title(self):
		"""
		A pretty title is a title starting with a capital followed by lowercase.
		"""
		p = Page(title = 'mijn titel')
		self.assertEquals(p.pretty_title(), 'Mijn titel')
		
				
				
				
