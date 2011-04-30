from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^monials/', include('monials.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^profiles/(?P<profile_id>\d+)/embed/$', 'testimonials.views.embed'),

    (r'^admin/', include(admin.site.urls)),
)
