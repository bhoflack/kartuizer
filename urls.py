from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		(r'^$', 'kartuizer.app.views.index'),
		(r'^admin/', include(admin.site.urls)),
		(r'^(?P<name>[a-zA-Z]*)$', 'kartuizer.app.views.page'),
		(r'^adminimages/(?P<path>.*)$', 'django.views.static.serve', 
			{'document_root': settings.IMAGES_ROOT}),
		)

if settings.DEBUG:
    urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
			{'document_root': settings.STATIC_DOC_ROOT}),
	)