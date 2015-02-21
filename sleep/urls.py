from django.conf.urls import patterns, url

from sleep import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
