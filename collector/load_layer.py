import os
from django.contrib.gis.utils import LayerMapping
from .models import Provinces, Districts

provinces_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'nl_name_1': 'NL_NAME_1',
    'varname_1': 'VARNAME_1',
    'geom': 'MULTIPOLYGON',
}

province_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/ZWE_adm1.shp'))

def run(verbose=True):
    lm = LayerMapping(Provinces, province_shp, provinces_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

districts_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'id_2': 'ID_2',
    'name_2': 'NAME_2',
    'type_2': 'TYPE_2',
    'engtype_2': 'ENGTYPE_2',
    'nl_name_2': 'NL_NAME_2',
    'varname_2': 'VARNAME_2',
    'geom': 'MULTIPOLYGON',
}

district_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/ZWE_adm2.shp'))

def district_import(verbose=True):
    lm = LayerMapping(Districts, district_shp, districts_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)