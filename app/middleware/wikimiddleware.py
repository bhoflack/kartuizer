# encoding: utf-8
"""
wikimiddleware.py

Translate wikipage to htmlpage.
"""

class WikiMiddleware:
	def process_response(self, request, response):
		"""Catch the wiki response and translate to html.
		
		   >>> response = MockHttpResponse("This is my wiki response [[url|text]]")
		   >>> wm = WikiMiddleware()
		   >>> wm.process_response(None, response)
			 >>> response.content
			 'This is my wiki response <a href="/url">text</a>'
		"""
		content = response.content
		replaced = content.replace("[[url|text]]", "<a href=\"/url\">text</a>")
		response.content = replaced

class MockHttpResponse:
	def __init__(self, response):
		self.content = response


if __name__ == "__main__":
	  import doctest
	  doctest.testmod()
	
