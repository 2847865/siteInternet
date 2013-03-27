from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^Toads/1$', views.page1, name='page1'),
	url(r'^Mortality/2$', views.page2, name='page2'),
	url(r'^Why/3$', views.page3, name='page3'),
	url(r'^media/crapaud.jpg$', views.page4, name='page4'),
	url(r'^page5/$', views.page5, name='page5'),
)