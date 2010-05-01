from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		(r'^admin/', include(admin.site.urls)),
		(r'^$', 'kartuizer.app.views.index'),
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
			{'document_root': settings.STATIC_DOC_ROOT})
)
