from django.http import HttpResponse
from django.template import Context, loader

from kartuizer.app.models import Page, MenuItem

def index(request):
		t = loader.get_template('index.html')
		p = Page.objects.get(pk=1)
		menuItems = MenuItem.objects.all()
		c = Context({'page' : p,
								 'menuitems': menuItems})
		
		return HttpResponse(t.render(c))