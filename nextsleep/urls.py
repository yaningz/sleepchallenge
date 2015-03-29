from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from nextsleep import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nextsleep.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('sleep.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/', 'mit.scripts_login', name='login', ),
    #url(r'^accounts/', include('registration.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
