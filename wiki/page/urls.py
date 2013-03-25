from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',
    url(r'^$', views.index, name=''),
	url(r'^page1/1$', views.page1, name='page1'),
	url(r'^page2/2$', views.page2, name='page2'),
	url(r'^page3/$', views.page3, name='page3'),
	url(r'^page4/$', views.page4, name='page4'),
	url(r'^page5/$', views.page5, name='page5'),
)