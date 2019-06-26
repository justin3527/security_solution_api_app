from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

  url(r'^admin/', include(admin.site.urls)),
  url(r'^solution/ise.html/$', views.ise, name='ise'),
  url(r'^solution/stw.html/$', views.stw, name='stw'),
  url(r'^solution/firepower.html/$', views.firePower, name='firepower'),
  url(r'^$', views.default, name='index'),

]
