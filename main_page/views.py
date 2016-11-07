#coding: utf8
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf

# Create your views here.

def new_ad(request):
	return HttpResponse('MAIN')

def show_current(request, ad_id):
	return HttpResponse('MAIN')

def show_billboard(request):
	args = {}
	return render_to_response('main.html')
	#return HttpResponse('MAIN')
