from arcgis.gis import *
from arcgis.features import FeatureLayer

admin_username = os.environ["ATLAS_AGO_ADMIN_USERNAME"]
admin_password = os.environ["ATLAS_AGO_ADMIN_PASSWORD"]

gis = GIS(username=admin_username, password=admin_password)

# URL of the map service layer you want to query
map_service_url = "https://utility.arcgis.com/usrsvcs/servers/[UNIQUE_ID]/rest/services/ATLAS/SUPPORT/MapServer/"

# Access the feature layer (layer 5)
layer_url = f"{map_service_url}/5"
layer = FeatureLayer(layer_url, gis=gis)

# Request a token
token = gis._con._token

# Define the query
where_clause = "(TRANSACTIONAL_RANCH_NUMBER = 18740 OR (TRANSACTIONAL_RANCH_NUMBER IS NULL AND RANCH_ID = 1281436)) AND (IS_ACTIVE IS NOT NULL AND IS_ACTIVE = 1)"

# Query the layer
query_result = layer.query(where=where_clause)

# Print the features
for feature in query_result.features:
    print(feature.attributes)