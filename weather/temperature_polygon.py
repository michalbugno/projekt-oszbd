from world.models import *
from django import db

points = Resorts.objects.filter(measuresresorts__measures__max_temp__lt=-10).unionagg().coords
points_string = ""

for point in points[:5]:
    # points.append((resort.position.x, resort.position.y))
    points_string += "%s, %s, " % (str(point[0]), str(point[1]))

points_string += "%s, %s " % (str(points[0][0]), str(points[0][1]))

#print points
#print points_string

c = db.connection.cursor()

a = c.execute('SELECT SDO_UTIL.TO_WKTGEOMETRY(MDSYS.SDO_GEOMETRY(2003, NULL, NULL, SDO_ELEM_INFO_ARRAY(1,2003,1), SDO_ORDINATE_ARRAY('+points_string+'))) FROM WORLD_WORLDBORDERS;').fetchone()[0].read()

print a
