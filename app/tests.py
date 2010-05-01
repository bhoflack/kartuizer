"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class WikiTest(TestCase):
    def test_url(self):
        """
        Tests that url is correctly translated.
        """
        urltext = """bestel a la carte of proef 
					van ons [[suggestiemenu|ons suggestiemenu]]."""
        expected = """bestel a la carte of proef van ons 
					<a href="/suggestiemenu">ons suggestiemenu</a>"""
					
        self.assertEquals(urltext, expected)
				
				
				
