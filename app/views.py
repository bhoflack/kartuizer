from django.http import HttpResponse
from django.template import Context, loader
import random

from kartuizer.app.models import Page, MenuItem, Review

def index(request):
	return page(request, 'home')
		
def page(request, name):
	t = loader.get_template('index.html')
	p = Page.objects.get(name=name)
	menuItems = MenuItem.objects.all()
	reviews = Review.objects.all()
	if len(reviews) > 0:
		samples = random.sample(reviews, 5)
	else:
		samples = []
	
	c = Context({
		'page': p,
		'menuitems': menuItems,
		'reviews': samples})
	return HttpResponse(t.render(c))