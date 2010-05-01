# encoding: utf-8
"""
wikimiddleware.py

Translate wikipage to htmlpage.
"""

from markdown import markdown

class WikiMiddleware:
	
	def process_response(self, request, response):
		"""Catch the wiki response and translate to html.
		
		>>> response = MockHttpResponse("This is my wiki response [text](url)")
		>>> wm = WikiMiddleware()
		>>> wm.process_response(None, response)
		http response
		>>> response.content
		u'<p>This is my wiki response <a href="url">text</a></p>'
		"""
		response.content = markdown(response.content) 
		return response

class MockHttpResponse:
	def __init__(self, response):
		self.content = response
		
	def __repr__(self):
		return "http response"


if __name__ == "__main__":
	  import doctest
	  doctest.testmod()
	
