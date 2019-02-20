from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

  url(r'^admin/', include(admin.site.urls)),
  url(r'^solution/$', views.index, name='solution'),
  url(r'^$', views.index, name='index'),
  url(r'^solution/new/$', views.post, name='solution'),
]
