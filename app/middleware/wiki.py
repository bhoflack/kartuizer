# encoding: utf-8
"""
wikimiddleware.py

Translate wikipage to htmlpage.
"""

class WikiMiddleware:
	
	def __init__(self, app, args):
		self.app = app
	
	def __call__(self, environ, start_response):
		"""Catch the wiki response and translate to html.
		
		   >>> response = MockHttpResponse("This is my wiki response [[url|text]]")
		   >>> wm = WikiMiddleware()
		   >>> wm.process_response(None, response)
			 >>> response.content
			 'This is my wiki response <a href="/url">text</a>'
		"""
		buffer = ""
		app_iter = self.app(environ, start_response)
		for line in app_iter:
			buffer.append(line)
		return [self.replace_wiki_words(buffer)] 
			 
			
	def replace_wiki_words(self, content):
		return content.replace("[[url|text]]", "<a href=\"/url\">text</a>")

class MockHttpResponse:
	def __init__(self, response):
		self.content = response


if __name__ == "__main__":
	  import doctest
	  doctest.testmod()
	
