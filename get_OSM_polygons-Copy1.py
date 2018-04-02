### home made functions
import nice_functions as nf

### other libraries

import pandas as pd

from shapely.ops import transform
from shapely.geometry import mapping, Polygon, box, shape
import matplotlib.pyplot as plt

from collections import namedtuple

import fiona

import pickle

from gbdxtools import Interface
from gbdxtools.task import env
from gbdxtools import CatalogImage

gbdx = Interface()


def get_OSM_polygons(city = 'Amsterdam',buffer_zone = 0,type_query = 'park',min_size = 1):

    ### set some parameters
    city = city

    buffer_zone = buffer_zone



    ## Use Google API to find coordinates of city
    bbox_city = nf.get_city_bounding_box(city)

    # get EPSG code and wgs/utm transformation information
    UTM_EPSG_code,project_utm,project_wgs = nf.get_projections_and_UTM(bbox_city)

    # query OSM vectors (results come back formatted as geojson) (choose from: water, forest, grass, park, footway,)
    geojson = nf.get_OSM_polygons(bbox_city = bbox_city,type_query = type_query)

    ### check polygon metadata like cloud cover, size, etc. and return the instances that pass the test sorted on area
    ### plus a list with all geometries 
    selection,geom_list = nf.geojson_variable_check(geojson,project_utm,min_size = min_size)

    # get only polygons that pass the above test as geojson
    geojson_select = []

    for id_nr in selection.id:
        geojson_select.append(geojson[id_nr])


    geom_list_selection = []

    for id_nr in selection.id:
        geom = shape(geojson[id_nr]['geometry'])
        geom_list_selection.append(geom)


    return selection, geojson_select, geom_list_selection