from django.conf.urls.defaults import *
from django.contrib.gis import admin
from django.views.generic.simple import direct_to_template
import os.path

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^weather/', include('weather.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'weather.world.views.map'),
    (r'^resort/(.+)/', 'weather.world.views.resort'),
    (r'^admin/(.*)', admin.site.root),
    (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'public').replace('\\','/')}),
)
