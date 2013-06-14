#!/usr/bin/env python

import sys
from os.path import dirname, join, splitext
from subprocess import call

# add the shapefiles dir to the path
shapefiles_path = join(dirname(__file__), 'shapefiles')
sys.path.append(shapefiles_path)

# load our shapefile definitions
from definitions import SHAPEFILES

if 'geojson' in sys.argv:
    for title, data in SHAPEFILES.items():
        shapefile = join('shapefiles', data['file'])
        geojsonfile = splitext(shapefile)[0] + '.geojson'
        proc = call(['ogr2ogr', '-f', 'geoJSON', geojsonfile, shapefile])
        print "* %s [source](%s) [map](%s)" % (
            title, data["href"], geojsonfile)
