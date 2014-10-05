from django.conf.urls import patterns, url

from SynthMuseum import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<m>[\w|\W]+)/(?P<n>[\w|\W]+)/$', views.detail, name='detail'),
                       )
