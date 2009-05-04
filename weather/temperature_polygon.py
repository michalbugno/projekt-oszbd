from world.models import *
from django import db

distance = Distance(km=15)
points = None

center_resort = Resorts.objects.all()[0]

points_data = Resorts.objects.filter(position__dwithin=(center_resort.position, distance), measuresresorts__measures__max_temp__lt=-10).exclude(pk=center_resort.pk).unionagg()

if points_data:
    points = points_data.coords

if points:
    print points

    #points = Resorts.objects.filter(measuresresorts__measures__max_temp__lt=-10).unionagg().coords

    points_string = str(points[:5] + points[0]).replace("(", "").replace(")", "")

    print points_string

    cursor = db.connection.cursor()
    sql = "SELECT SDO_UTIL.TO_WKTGEOMETRY(MDSYS.SDO_GEOMETRY(2003, NULL, NULL, SDO_ELEM_INFO_ARRAY(1,2003,1), SDO_ORDINATE_ARRAY(%s))) FROM WORLD_WORLDBORDERS;" % (points_string)
    cursor.execute(sql)
    output = cursor.fetchone()[0]

    print output
else:
    print 'POLYGON (())'
