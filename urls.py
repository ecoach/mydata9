from django.conf.urls.defaults import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import redirect_to

#from mycoach import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # login / logout
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    # staff apps
    url(r'^staff/',         include('mypublisher.urls', namespace='mystaff')),
    url(r'^publisher/',     include('mypublisher.urls', namespace='mypublisher')),
    url(r'^usage/',         include('myusage.urls', namespace='myusage')),
    #url(r'^upload/',        include('myloader.urls', namespace='myloader')),
    #url(r'^emailer/',       include('myemailer.urls', namespace='myemailer')),
    #url(r'^copycat/',       login_required(mycopycat.urls)),
    #url(r'^download/',      login_required(myextractor.urls)),
    #url(r'^curator/',       login_required(mycurator.urls)),
    #url(r'^logger/',        login_required(mylogger.urls)),

    # message project
    #url(r'^',               include('mycoach.urls', namespace='mycoach')),
    url(r'^',               include('mycoach.urls', namespace='mycoach')),
)

