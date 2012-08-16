# Create your views here.

from django.template import loader
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.shortcuts import render_to_response, redirect

def get_home(request):
    return render_to_response('home.html',context_instance=RequestContext(request))

def get_timeline(request):
    return render_to_response('timeline.html',context_instance=RequestContext(request))

