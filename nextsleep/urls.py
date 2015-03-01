from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nextsleep.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('sleep.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'mit.scripts_login', name='login', ),
)
