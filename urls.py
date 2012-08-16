from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from website import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', redirect_to, {'url':'/home/'}),
                       url(r'^s/(?P<path>.*)$', 'django.views.static.serve', 
                           { 'document_root': settings.STATIC_ROOT, }),
                       url(r'^timeline/$', views.get_timeline, name='timeline'),
                       url(r'^home/$', views.get_home, name='home'),
                           # url(r'^bw/', include('bw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
