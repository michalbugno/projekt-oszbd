# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from world.models import Resorts

def map(request):
  resorts = Resorts.objects.all()
  resorts = Resorts.objects.all()
  return render_to_response('map.html', {'resorts' : resorts})
