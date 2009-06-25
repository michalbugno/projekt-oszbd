# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from world.models import Resorts
import os

import datetime

resorts_list = Resorts.objects.all()

def map(request):
  resorts = Resorts.objects.all()
  resorts = Resorts.objects.all()
  return render_to_response('map.html', {'resorts' : resorts})

def resort(request, resort_pk):
  resorts = Resorts.objects.filter(pk=resort_pk)
  if len(resorts) != 1:
    return HttpResponse("Not found")
  else:
    resort = resorts[0]
    within = int(request.GET.get('within', 20))
    near_resorts = resort.within_distance(within)
    return render_to_response('resort.html', {'resort' : resort, 'near_resorts' : near_resorts, 'within' : within})

def isotherms(request):
    global resorts_list

    if request.GET:
        p_resort = Resorts.objects.get(pk=request.GET['resort'])

        day = int(request.GET['day'])
        month = int(request.GET['month'])
        year =int(request.GET['year'])

        chosen_date = datetime.date(year, month, day)

        prev_date = datetime.date.fromordinal(chosen_date.toordinal()-1)
        next_date = datetime.date.fromordinal(chosen_date.toordinal()+1)

        shortpath = 'iso_%s_%02d-%02d-%02d.png' % (p_resort.name, year, month, day)
        path = 'public/'+shortpath

        query_dict = {  'path' : shortpath,
                'p_resort' : p_resort.name,
                'day' : str(day),
                'month' : str(month),
                'year'  : str(year),
                'n_day' : str(next_date.day),
                'n_month' : str(next_date.month),
                'n_year'  : str(next_date.year),
                'p_day' : str(prev_date.day),
                'p_month' : str(prev_date.month),
                'p_year'  : str(prev_date.year),
                'resorts_list' : resorts_list,
        }
    
        if not os.path.exists(path):
            second, third = p_resort.find_far(chosen_date)
            p_resort.draw_isoterms(chosen_date, 8, 60, path)
            second.draw_isoterms(chosen_date, 8, 100, path, new_im=False)
            third.draw_isoterms(chosen_date, 8, 100, path, new_im=False)

        return render_to_response('isotherms.html', query_dict)

    else:
        render_errors = 'no request'
        return render_to_response('isotherms.html', {'render_errors' : render_errors, 'resorts_list' : resorts_list})




