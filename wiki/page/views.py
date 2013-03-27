from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	return render(request, 'page/homepage.html')
def page1(request):
	return render(request, 'page/page1.html')
def page2(request):
	return render(request, 'page/page2.html')
def page3(request):
	return HttpResponse("page3 !!!")
def page4(request):
	return HttpResponse("page4 !!!")
def page5(request):
	return HttpResponse("page5 !!!")
# Create your views here.
