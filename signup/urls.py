from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

from signup import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
)