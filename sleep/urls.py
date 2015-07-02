from django.conf.urls import patterns, url

from sleep import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^record/$', views.record, name='record'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginUser/$', views.loginUser, name='loginUser'),
)
