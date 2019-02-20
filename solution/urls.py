from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
  url(r'^$', views.test, name='test'),
  url(r'^solution/$', views.index, name='solution'),
  url(r'^$', views.index, name='index'),
  url(r'^solution/new/$', views.post, name='solution'),
]
