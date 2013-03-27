from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from page.models import Page

def index(request):
  p = Page.objects.get(pk = 1)   
  template = loader.get_template('page/homepage.html')
  context = Context({
    'page': p,
  })
  return HttpResponse(template.render(context))

def page1(request):
  p = Page.objects.get(pk = 2)   
  template = loader.get_template('page/page1.html')
  context = Context({
    'page': p,
  })
  return HttpResponse(template.render(context))
  
def page2(request):
  p = Page.objects.get(pk = 3)   
  template = loader.get_template('page/page2.html')
  context = Context({
    'page': p,
  })
  return HttpResponse(template.render(context))
def page3(request):
	return render(request, 'page/page3.html')
def page4(request):
	return HttpResponse("page4 !!!")
def page5(request):
	return HttpResponse("page5 !!!")
# Create your views here.
