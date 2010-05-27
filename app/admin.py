from kartuizer.app.models import Page, MenuItem, Review
from django.contrib import admin

class MenuItemAdmin(admin.ModelAdmin):
	ordering = ['position']
	
class PageAdmin(admin.ModelAdmin):
	
	class Media:
	        js = ( '/js/wmd/wmd.js', )
	
admin.site.register(Page, PageAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Review)