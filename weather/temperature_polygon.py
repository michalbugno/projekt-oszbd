from world.models import *
from django import db

points = Resorts.objects.filter(measuresresorts__measures__max_temp__lt=-10).unionagg().coords

points_string = str(points[:5] + points[0]).replace("(", "").replace(")", "")

cursor = db.connection.cursor()
sql = "SELECT SDO_UTIL.TO_WKTGEOMETRY(MDSYS.SDO_GEOMETRY(2003, NULL, NULL, SDO_ELEM_INFO_ARRAY(1,2003,1), SDO_ORDINATE_ARRAY(%s))) FROM WORLD_WORLDBORDERS;" % (points_string)
cursor.execute(sql)
output = cursor.fetchone()[0]

print output
