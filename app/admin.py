from kartuizer.app.models import Page, MenuItem
from django.contrib import admin

class MenuItemAdmin(admin.ModelAdmin):
	ordering = ['position']
	
admin.site.register(Page)
admin.site.register(MenuItem, MenuItemAdmin)