# run with ArcGIS API for Python 3

# Find an address using ArcGIS World Geocoding Service

from arcgis.gis import *
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point

# Log into ArcGIS Online as an anonymous user
dev_gis = GIS()

# Search for the Hollywood sign
geocode_result = geocode(address="200 Lincoln Ave Salinas CA", as_featureset=True)
print(geocode_result)


# Reverse geocode a coordinate
print("")
location = {'Y':36.67526264843514,'X':-121.65731271093892,
    'spatialReference':{
        'wkid':4326
    }
}
unknown_pt = Point(location)

address = reverse_geocode(location=unknown_pt)
print(address)
