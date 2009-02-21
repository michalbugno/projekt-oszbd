# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from world.models import Resorts

def map(request):
  resorts = Resorts.objects.all()
  resorts = Resorts.objects.all()
  return render_to_response('map.html', {'resorts' : resorts})

def resort(request, resort_pk):
  pk = int(resort_pk)
  resorts = Resorts.objects.filter(pk=pk)
  if len(resorts) != 1:
    return HttpResponse("Not found")
  else:
    resort = resorts[0]
    near_resorts = resort.within_distance(20)
    return render_to_response('resort.html', {'resort' : resort, 'near_resorts' : near_resorts})
