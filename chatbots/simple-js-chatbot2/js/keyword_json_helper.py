import json, os, sys, re

map_gallery_table = {
    'https://www.cityofsalinas.org/map/airport-influence-area' : ['Airport', 'Airport Influence Area', 'Salinas Municipal Airport', 'Land Use', 'Zoning', 'City of Salinas', 'AIA', 'Zoning Overlay', 'Runway Protection Zones', 'RPZ', 'Airplane', 'Municipal Airport'],
    'https://www.cityofsalinas.org/map/alisal-vibrancy-plan-area' : ['Alisal', 'Alisal Vibrancy Plan', 'Vision Salinas', 'Alisal Area', 'Alisal Plan', 'Alisal Revitilization Plan', 'Community Planning', 'Alisal Neighborhood'],
    'https://www.cityofsalinas.org/map/bikeways' : ['City of Salinas', 'City of Salinas Bikeways', 'Bike Plan', 'Bicycle Routes', 'Bikeways', 'Bike Path', 'Bike Route', 'Traffic and Transportation', 'Alternative Transportation', 'Recreation', 'Bicycle Committee'],
    'https://www.cityofsalinas.org/map/burglary' : ['Burglary', 'Crime Rate', 'Police Department', 'Crime', 'Burglary Rate', 'Police', 'Crime Information'],
    'https://www.cityofsalinas.org/map/census-blocks-2010' : ['Census Blocks', '2010 Census', 'Census', '2010 Census Blocks', 'Blocks', '2010'],
    'https://www.cityofsalinas.org/map/census-tracts-2010' : ['2010 Census', 'Public Works', 'Census Tracts', 'Census', 'Tracts', 'Census Bureau'],
    'https://www.cityofsalinas.org/map/chinatown' : ['Chinatown', 'Revitalization', 'Plan', 'Community Development', 'Chinatown Revitalization Plan', 'Community Planning'],
    'https://www.cityofsalinas.org/map/city-boundary' : ['City of Salinas', 'City of Salinas Boundary', 'Boundary', 'City Limits', 'City', 'Public Works', 'City Boundary'],
    'https://www.cityofsalinas.org/map/city-owned-developedundeveloped-parcels' : ['City Owned Parcels', 'Parcels', 'City Parcels', 'Planning', 'Developed Parcels', 'Undeveloped Parcels', 'Parcel'],
    'https://www.cityofsalinas.org/map/contours-topography' : ['Contours', 'Topography', 'Height', 'Elevation', 'Isoheight', 'GIS'],
    'https://www.cityofsalinas.org/map/council-districts' : ['City of Salinas', 'District', 'City of Salinas City Council District', 'City Council', 'Council District', 'Council', 'Council Members'],
    'https://www.cityofsalinas.org/map/crosswalks' : ['Crosswalks', 'Street Crossings', 'Traffic and Transportation', 'Pedestrian Crosswalks', 'Crossover'],
    'https://www.cityofsalinas.org/map/downtown-parking-0' : ['Downtown Parking', 'Parking', 'Parking Lot', 'Downtown'],
    'https://www.cityofsalinas.org/map/existingplanned-transit-stops' : ['Transit', 'Traffic and Transportation', 'Bus Stops', 'Transit Stops', 'Bus', 'Public Transportation'],
    'https://www.cityofsalinas.org/map/family-resourcecommunity-centers' : ['Family Center', 'Family Resource Center', 'Community Center', 'Community Services', 'Recreation and Community Services'],
    'https://www.cityofsalinas.org/map/fema-flood-map' : ['City of Salinas', 'Flood Zone', 'Flood', 'FEMA', 'NFHL', 'National Flood Hazard', 'Federal Emergency Management Agency', 'Emergency'],
    'https://www.cityofsalinas.org/map/fire-stations' : ['City of Salinas', 'Fire Houses', 'Fire Stations', 'Safety', 'Fire Department', 'Fire'],
    'https://www.cityofsalinas.org/map/focused-growth-areas' : ['City of Salinas', 'City of Salinas Focused Growth Areas', 'FGA', 'Focused Growth Area'],
    'https://www.cityofsalinas.org/map/future-growth-area' : ['Future Growth Area', 'Growth', 'Future Growth Boundary', 'Community Development', 'Community Planning', 'City Boundary', 'Planning'],
    'https://www.cityofsalinas.org/map/gateways' : ['City of Salinas', 'Gateway Overlay Districts', 'Zoning', 'Planning', 'Gateway'],
    'https://www.cityofsalinas.org/map/general-plan-circulation-network' : ['General Plan', 'Circulation Network', 'General Plan Info', 'General Plan Circulation Network'],
    'https://www.cityofsalinas.org/map/height-restricted-roadways' : ['Height Restricted Roadway', 'Vertical Clearances', 'Vertical', 'Height Limit', 'Clearance', 'Overpass Height', 'Overpass'],
    'https://www.cityofsalinas.org/map/hospitals' : ['Hospitals', 'Medical Center', 'Emergency', 'Hospital', 'Emergency Medical Services'],
    'https://www.cityofsalinas.org/map/impervious-surfaces' : ['Impervious Surface', 'Land Cover', 'Impenetrable Surface', 'Surface', 'Runoff', 'Water', 'Stormwater', 'Waste/Water and Energy'],
    'https://www.cityofsalinas.org/map/law-enforcement' : ['City of Salinas', 'Police', 'Sheriff', 'Law Enforcement', 'Highway Patrol', 'Safety', 'Police Stations', 'Police Department'],
    'https://www.cityofsalinas.org/map/libraries' : ['Libraries', 'Library', 'Public Library', 'Education', 'Salinas Public Library', 'Community Development'],
    'https://www.cityofsalinas.org/map/maintenance-districts' : ['District', 'Maintenance Districts', 'City of Salinas', 'Assessment Districts'],
    'https://www.cityofsalinas.org/map/monterey-county-cities' : ['Monterey County Boundary', 'Monterey Cities', 'County', 'Monterey Boundary', 'Planning', 'Monterey County Cities'],
    'https://www.cityofsalinas.org/map/parks-and-recreation-centers' : ['City of Salinas', 'Parks', 'Recreation', 'Open Space', 'Parks and Recreation'],
    'https://www.cityofsalinas.org/map/pedestrianbikeautomobile-collisions' : ['Collision', 'Automobile Collision', 'Pedestrian Collision', 'Bike collision', 'Traffic and Transportation', 'Car Crashes', 'Automobile Accidents'],
    'https://www.cityofsalinas.org/map/police-command-areas' : ['Police Command Areas', 'Command Areas', 'Police Department', 'Police Response Area', 'Police'],
    'https://www.cityofsalinas.org/map/public-properties' : ['Public Properties', 'Community Planning', 'Public'],
    'https://www.cityofsalinas.org/map/radar-surveys' : ['Radar Surveys', 'Traffic Surveys', 'Traffic and Engineering Surveys', 'Radar', 'Survey', 'Traffic and Transportation', 'California Highway Patrol'],
    'https://www.cityofsalinas.org/map/railroad' : ['Railroad', 'Rail Lines', 'Amtrak', 'Transportation', 'Public Transportation', 'Railroad Lines'],
    'https://www.cityofsalinas.org/map/roadway-centerlines' : ['City of Salinas', 'Roadway Centerlines', 'Roadway', 'Roads', 'Streets', 'City Streets', 'Road', 'Transportation', 'Centerlines'],
    'https://www.cityofsalinas.org/map/robbery' : ['Police Department', 'Crime Rate', 'Robbery', 'Police', 'Crime', 'Robbery Crime Rate'],
    'https://www.cityofsalinas.org/map/school-districts' : ['City of Salinas', 'School District', 'Education', 'Districts', 'School', 'Salinas Schools'],
    'https://www.cityofsalinas.org/map/schools' : ['City of Salinas', 'Education', 'Schools', 'High Schools', 'Elementary', 'College'],
    'https://www.cityofsalinas.org/map/sidewalk-conditions' : ['Sidewalk', 'Sidewalk Conditions', 'Transportation', 'Community Development', 'Public Works'],
    'https://www.cityofsalinas.org/map/solar-irradiance' : ['Solar', 'irradiance', 'Insolation', 'Power'],
    'https://www.cityofsalinas.org/map/specific-plan-areas' : ['City of Salinas', 'City of Salinas Specific Plan Areas', 'SPA', 'General Plan', 'Specific Plan Areas', 'Planning'],
    'https://www.cityofsalinas.org/map/speed-limit' : ['Speed Limit', 'Traffic and Transportation', 'Traffic', 'Speed', 'Limit'],
    'https://www.cityofsalinas.org/map/sphere-influence' : ['City of Salinas', 'Sphere of Influence', 'SOI', 'General Plan', 'Zoning', 'Zoning Overlay'],
    'https://www.cityofsalinas.org/map/street-lights' : ['Street Lights', 'Community Development', 'Sidewalk', 'Traffic and Transportation', 'Transportation', 'Light', 'Alternative Transportation'],
    'https://www.cityofsalinas.org/map/street-signs' : ['Street Signs', 'Traffic and Transportation', 'Traffic', 'Streets', 'Transportation'],
    'https://www.cityofsalinas.org/map/suba-boundary' : ['City of Salinas', 'SUBA', 'Salinas United Business Association', 'Business', 'Zoning', 'Zoning Overlay'],
    'https://www.cityofsalinas.org/map/subdivisions' : ['Subdivisions', 'Community Development', 'Planning', 'Housing', 'Subdivision Index'],
    'https://www.cityofsalinas.org/map/subwatersheds' : ['Subwatershed', 'Urban Watershed', 'Stormwater', 'Water', 'Watershed', 'Waste/Water and Energy'],
    'https://www.cityofsalinas.org/map/survey-benchmarks' : ['Survey', 'Benchmarks', 'Survey Benchmarks', 'surveying'],
    'https://www.cityofsalinas.org/map/survey-markers' : ['Survey Markers', 'Survey', 'Benchmarks', 'NGS', 'National Geodetic Survey', 'Survey Monuments'],
    'https://www.cityofsalinas.org/map/traffic-calming' : ['Traffic and Transportation', 'Traffic Calming', 'Traffic', 'Speed Bumps', 'Speed Cushions', 'Traffic Circle', 'Striping', 'Roundabout'],
    'https://www.cityofsalinas.org/map/traffic-counts-signalized-intersections' : ['Traffic Signals', 'Traffic and Transportation', 'Signals', 'Traffic Lights', 'Intersections', 'Traffic Counts'],
    'https://www.cityofsalinas.org/map/traffic-volumes' : ['Transportation', 'Street Traffic', 'Traffic Volumes', 'Traffic Counts', 'Traffic and Transportation'],
    'https://www.cityofsalinas.org/map/truck-routes' : ['Truck Routes', 'Commercial Trucks', 'Commercial Truck Network', 'Truck Routing', 'Commercial Truck Routes', 'Traffic and Transportation'],
    'https://www.cityofsalinas.org/map/vacant-land' : ['Vacant Land', 'Vacant', 'Undeveloped Land', 'Planning Commission', 'Planning', 'Community Planning'],
    'https://www.cityofsalinas.org/map/vehicle-theft' : ['Police Department', 'Vehicle Thefts', 'Crime Rate', 'Police', 'Crime Information', 'Crime', 'Car Theft'],
    'https://www.cityofsalinas.org/map/walkability-parks' : ['Parks', 'Walkability Park', 'Urban Green Program', 'Neighborhood Vibrancy', 'Open Space'],
    'https://www.cityofsalinas.org/map/water-purveyordistrict' : ['Water Purveyor', 'Water District', 'Water', 'water Company', 'Purveyor', 'Cal Water', 'Alco Water'],
    'https://www.cityofsalinas.org/map/zip-codes' : ['City of Salinas', 'Zip Code', 'Zip', 'Postal Code', 'City of Salinas Zip Codes'],
    'https://www.cityofsalinas.org/map/zoning' : ['Zoning', 'Planning', 'Community Development', 'Zones', 'Permit', 'Current Planning'],
    'https://www.cityofsalinas.org/map/zoning-overlay-districts' : ['City of Salinas', 'Zoning', 'Overlay', 'District', 'Zoning Overlay', 'Zoning Overlay Districts'],
}

misc_keyword_data = {
    'GIS' : {
        'links' : {
            'City of Salinas GIS Division' : ['https://www.cityofsalinas.org/our-city-services/public-works/gis-services'],
            'Salinas Storymaps' : ['https://giswebservices.ci.salinas.ca.us/storymaps/dashboard/'],
            'City of Salinas Map Gallery' : ['https://www.cityofsalinas.org/our-government/information-center/map-gallery'],
            'City of Salinas Open Data Portal' : ['https://cityofsalinas.opendatasoft.com/pages/homepage/']
        }
    },
    'Map Gallery' : {
        'links' : {
            'Salinas Map Gallery' : ['https://www.cityofsalinas.org/our-government/information-center/map-gallery']
        }
    },
    'Open Data Portal' : {
        'links' : {
            'Open Data Portal Homepage' : ['https://cityofsalinas.opendatasoft.com/pages/homepage/']
        }
    },
    'Story Maps' : {
        'links' : {
            'Story Maps' : ['https://giswebservices.ci.salinas.ca.us/storymaps/dashboard/']
        }
    },
    'Salinas' : {
        'links' : {
            'City of Salinas Homepage' : ['https://www.cityofsalinas.org/'],
            'Storymaps' : ['https://giswebservices.ci.salinas.ca.us/storymaps/dashboard/']
        }
    },
    'Traffic and Transportation' : {
        'links' : {
            'Salinas Traffic Calming Projects Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/trafficcalmingprojects/'],
            'Salinas Downtown Complete Streets Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/downtowncompletestreets/'],
            'Salinas Roundabouts Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/salinasroundabouts/']
        }
    },
    'Traffic' : {
        'links' : {
            'Salinas Traffic Calming Projects Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/trafficcalmingprojects/'],
            'Salinas Downtown Complete Streets Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/downtowncompletestreets/'],
            'Salinas Roundabouts Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/salinasroundabouts/']
        }
    },
    'Traffic Calming' : {
        'links' : {
            'Salinas Traffic Calming Projects Story Map' : ['https://giswebservices.ci.salinas.ca.us/storymaps/trafficcalmingprojects/']
        }
    }
}

odp_keywords = [
    'Quality of Life',
    'City of Salinas',
    'Transportation and Infrastructure',
    'Library',
    'Planning and Community Engagement',
    'Safety',
    'High Performing Government',
    'Economic Development',
    'Parks and Recreation',
    'Recreation Centers',
    'Salinas',
    'Water',
    '(AIA)',
    'Airport Influence Area',
    'Alisal Vibrancy Plan',
    'Fire',
    'Police',
    'Public Works',
    'Salinas Municipal Airport',
    'Survey',
    'Vision Salinas',
    'landuse',
    'zoning overlay',
    'Alisal',
    'Alisal District',
    'Alternative Transportation',
    'Bench Mark',
    'Benchmark',
    'Bicycle',
    'Bike',
    'Bike Plan',
    'Bike Route',
    'Bike path',
    'Bikepath',
    'Bikeway',
    'Centerline',
    'City of Salinas Boundary',
    'Community Center',
    'Community Centers',
    'Community Development',
    'Community Services',
    'Council Districts',
    'Emergency Response',
    'FEMA',
    'Facilities',
    'Family Center',
    'Family Resource Center',
    'Federal Emergency Management Agency',
    'Fire Department',
    'Fire House',
    'Fire Station',
    'Firefighter',
    'Flood',
    'Flood Hazard',
    'Flood Zone',
    'Floodway',
    'GPS',
    'GPS Control Network',
    'General Plan',
    'Half Mile',
    'Intersection Counts',
    'Intersections',
    'KPI',
    'Landmarks',
    'Monument',
    'NFHL',
    'NGS',
    'NTMP',
    'National Flood Hazard Layer',
    'National Geodetic Survey',
    'Neighborhood Traffic Management Program',
    'Neighborhood Vibrancy',
    'Open',
    'Open Space',
    'Park',
    'Parks',
    'Recreation Center',
    'Road',
    'Road Centerline',
    'Roundabouts',
    'Salinas Parks',
    'Signalized Intersections',
    'Space',
    'Speed Bumps',
    'Survey Marker',
    'Traffic',
    'Traffic Calming',
    'Traffic Circle',
    'Traffic Counts',
    'Traffic Signals',
    'Traffic Survey',
    'Transportation',
    'Urban Design',
    'Walk',
    'Walkability',
    'Youth Centers',
    'beta release',
    'building',
    'planning',
    'zoning'
]

published_services = [
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/10ftContours/MapServer', '10ft Contours'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/2010_Census_Blocks/MapServer', '2010 Census Blocks'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/2010_Census_Tract_8x11/MapServer', '2010 Census Tract 8x11'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Airport_Overlay_Dist/MapServer', 'Airport Overlay District'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/AlisalStrategyArea/MapServer', 'Alisal Strategy Area'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/AllSalinasSchoolDistricts/FeatureServer', 'All Salinas School Districts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/AllSalinasSchoolDistricts/MapServer', 'All Salinas School Districts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Anonymized_Crime_Data/MapServer', 'Anonymized Crime Data'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/AverageDailySolarIrradiance/MapServer', 'Average Daily Solar Irradiance'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Bikeways/MapServer', 'Bikeways'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/BroadbandOpenData/MapServer', 'Broadband Open Data'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Burglary_heatmap_8x11/MapServer', 'Burglary heatmap 8x11'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Census_HTC/MapServer', 'Census HTC'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Chinatown/MapServer', 'Chinatown'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/City_boundary/MapServer', 'City boundary'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/CityOwnedParcels2017/MapServer', 'City Owned Parcels 2017'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Collisions/MapServer', 'Collisions'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Council_Districts/MapServer', 'Council Districts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Crosswalks/MapServer', 'Crosswalks'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/CurrentSweeperRoutes/MapServer', 'Current Sweeper Routes'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/DetentionBasinsandAreas/MapServer', 'Detention Basins and Areas'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/DowntownParking/MapServer', 'Downtown Parking'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Engineering_and_Traffic_Surveys/MapServer', 'Engineering and Traffic Surveys'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/FAAAirspace/MapServer', 'FAA Airspace'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/FamilyResourceCommunityCenters/MapServer', 'Family Resource Community Centers'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/FEMA/MapServer', 'FEMA'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Fire_Stations/MapServer', 'Fire Stations'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/FireRunsOpenData/MapServer', 'Fire Runs Open Data'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Focused_growth_areas/MapServer', 'Focused growth areas'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Future_Growth_Area/MapServer', 'Future Growth Area'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Gateway/MapServer', 'Gateway'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/GP02CirculationNetwork/MapServer', 'GP02 Circulation Network'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/GroceryStoreLocationsEdit/FeatureServer', 'Grocery Store Locations Edit'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/GroceryStoreLocationsEdit/MapServer', 'Grocery Store Locations Edit'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/GroceryStoreLocations/MapServer', 'Grocery Store Locations'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/HeightRestrictedRoadways/MapServer', 'Height Restricted Roadways'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/HistoricAnnexations/MapServer', 'Historic Annexations'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/HistoricResources/MapServer', 'Historic Resources'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Hospitals/MapServer', 'Hospitals'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/ImperviousSurface2016/MapServer', 'Impervious Surface 2016'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Law_Enforcement/MapServer', 'Law Enforcement'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/LED_street_lights/MapServer', 'LED street lights'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Libraries/MapServer', 'Libraries'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/LibrariesOpenData/FeatureServer', 'Libraries Open Data'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/LibrariesOpenData/MapServer', 'Libraries Open Data'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/LibraryPoints/MapServer', 'Library Points'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/MaintenanceDistricts/MapServer', 'Maintenance Districts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Monterey_County_Cities/MapServer', 'Monterey County Cities'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/MSTStops/MapServer', 'MST Stops'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Neighborhod_Watch_boundaries/MapServer', 'Neighborhod Watch boundaries'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/OpportunityZones/FeatureServer', 'Opportunity Zones'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/OpportunityZones/MapServer', 'Opportunity Zones'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Parks/FeatureServer', 'Parks'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Parks/MapServer', 'Parks'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Police_Command_Areas/MapServer', 'Police Command Areas'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/PoliceBeats/MapServer', 'Police Beats'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Projected_Township_Ranges/MapServer', 'Projected Township Ranges'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/PublicProperties/MapServer', 'Public Properties'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/RailLines/MapServer', 'Rail Lines'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Roadway_Centerlines/MapServer', 'Roadway Centerlines'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Robbery_Heatmap/MapServer', 'Robbery Heatmap'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/School_Districts/MapServer', 'School Districts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Schools/MapServer', 'Schools'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Sidewalk/MapServer', 'Sidewalk'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/SidewalkSchedule/MapServer', 'Sidewalk Schedule'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/SignalizedIntersectionCounts/MapServer', 'Signalized Intersection Counts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Specific_plan_areas/MapServer', 'Specific plan areas'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/SpeedLimit/MapServer', 'Speed Limit'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Sphere_of_influence/MapServer', 'Sphere of influence'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/street_sign_8x11/MapServer', 'street sign 8x11'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/SUBA/MapServer', 'SUBA'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Subdivisions/MapServer', 'Subdivisions'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Subwatersheds_layer/MapServer', 'Subwatersheds layer'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Subwatersheds/MapServer', 'Subwatersheds'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Survey_Markers_8x11/MapServer', 'Survey Markers 8x11'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/SurveyBenchmarks/MapServer', 'Survey Benchmarks'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TrafficCalming1/MapServer', 'Traffic Calming 1'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TrafficCalming/MapServer', 'Traffic Calming'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TrafficIssueDatabase/FeatureServer', 'Traffic Issue Database'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TrafficIssueDatabase/MapServer', 'Traffic Issue Database'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TrafficVolumeCounts/MapServer', 'Traffic Volume Counts'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TransitStops/MapServer', 'Transit Stops'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/TruckRoute/MapServer', 'Truck Route'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/USGS_24k_Quad_Topo_Index/MapServer', 'USGS 24k Quad Topo Index'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/VacantLand/MapServer', 'Vacant Land'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Vehicle_Theft_Heatmap_8X11/MapServer', 'Vehicle Theft Heatmap 8X11'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Walkability_Parks_Within_HalfMile/MapServer', 'Walkability Parks Within HalfMile'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Walkability_parks/MapServer', 'Walkability parks'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/WaterPurveyors/MapServer', 'Water Purveyors'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Waterways/MapServer', 'Waterways'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Zip_Codes/MapServer', 'Zip Codes'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Zoning/MapServer', 'Zoning'],
    ['https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/ZoningOverlayDistrictsAll/MapServer', 'Zoning Overlay Districts All'],
]


def normalize_keyword(keyword_str):
    '''
    Normalize the titles using common title capitalization rules
    '''

    lower_case_words = ['a', 'an', 'and', 'at', 'but', 'by', 'for', 'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet']

    abbreviations = ['(aia)', 'aia', 'fema', 'gps', 'kpi', 'nfhl', 'ngs', 'ntmp', 'rpz', 'gis', 'fga', 'spa', 'soi', 'suba']

    result = keyword_str.lower()

    tokens = result.split()

    for i in range(len(tokens)):
        token = tokens[i]
        if (i == 0) or (i == (len(tokens) - 1)):
            tokens[i] = tokens[i].capitalize()

        if token not in lower_case_words:
            tokens[i] = tokens[i].capitalize()

        if token in abbreviations:
            tokens[i] = tokens[i].upper()

    return ' '.join(tokens)

# for keyword in odp_keywords:
#     print(normalize_keyword(keyword))

# sys.exit()




# a mapping from keywords to a list of links
keyword_to_map_gallery_link_hash = {}

# construct keyword_to_map_gallery_link_hash
for url in map_gallery_table:
    keywords = map_gallery_table[url]

    for keyword in keywords:
        normalized_keyword = normalize_keyword(keyword)

        if normalized_keyword not in keyword_to_map_gallery_link_hash:
            keyword_to_map_gallery_link_hash[normalized_keyword] = [url]
        else:
            if url not in keyword_to_map_gallery_link_hash[normalized_keyword]:
                keyword_to_map_gallery_link_hash[normalized_keyword].append(url)

keyword_json_dict = {}

# construct keyword_json_dict
for keyword in keyword_to_map_gallery_link_hash:
    value = {
        'links' : {
            'Map Gallery' : []
        }
    }

    urls = keyword_to_map_gallery_link_hash[keyword]

    for url in urls:
        value['links']['Map Gallery'].append(url)

    keyword_json_dict[keyword] = value

# add misc keyword data to keyword json dict
for keyword in misc_keyword_data:
    normalized_keyword = normalize_keyword(keyword)

    links = misc_keyword_data[keyword]['links']

    if normalized_keyword not in keyword_json_dict:
        keyword_json_dict[normalized_keyword] = misc_keyword_data[keyword]
    else:
        for key in links:
            val = links[key]
            keyword_json_dict[normalized_keyword]['links'][key] = val


def get_regex_string(keyword):
    result = re.sub(r'\s+', r'\s*-?\s*', keyword.lower())
    return result


for keyword in odp_keywords:
    normalized_keyword = normalize_keyword(keyword)

    if normalized_keyword not in keyword_json_dict:
        keyword_json_dict[normalized_keyword] = {}


for key in keyword_json_dict:
    normalized_key = normalize_keyword(key)

    regex = get_regex_string(normalized_key)

    keyword_json_dict[key]['regExpr'] = regex
    keyword_json_dict[key]['odpQueryString'] = normalized_key.lower()


# modify special cases



'''

City of Salinas
    - mirror w/ salinas
    - link to city website
    - link to odp homepage

Combine all bike stuff

combine all recreation / park 
    + parks storymap link

Make sure odp queries return results?

'''

def combine_keywords_in_keyword_json_dict(json_dict, keywords, new_keyword, new_regexp):
    '''
    Combine the values in json_dict for a list of keywords, and store them as the value for new_keyword,
    with a new regular expression new_regexp
    '''
    new_links = {}
    for key in keywords:
        normalized_key = normalize_keyword(key)

        if 'links' in json_dict[normalized_key]:

            curr_links = json_dict[normalized_key]['links']
            for k in curr_links:
                if k not in new_links:
                    new_links[k] = curr_links[k]
                else:
                    new_links[k] += [x for x in curr_links[k] if x not in new_links[k]]

        del json_dict[normalized_key]

    json_dict[normalize_keyword(new_keyword)] = {
        'links' : new_links,
        'regExpr' : new_regexp,
        'odpQueryString' : normalize_keyword(new_keyword).lower()
    }

    return

combine_keywords_in_keyword_json_dict(keyword_json_dict, ['City of Salinas', 'Salinas'], 'Salinas', 'salinas')

combine_keywords_in_keyword_json_dict(keyword_json_dict, ['City of Salinas Bikeways', 'Bike Plan', 'Bicycle Routes',
    'Bikeways', 'Bike Path', 'Bike Route', 'Bicycle Committee', 'Bike Collision', 'Bicycle', 'Bike', 'Bikepath', 'Bikeway'], 'bike', '(bike|bicycle)')

combine_keywords_in_keyword_json_dict(keyword_json_dict, ['Parks', 'Walkability Park', 'Park', 'Salinas Parks'], 'Parks', 'parks?')

combine_keywords_in_keyword_json_dict(keyword_json_dict, ['Recreation', 'Recreation and Community Services', 'Parks and Recreation', 'Recreation Centers', 'Recreation Center'], 'Recreation', r'rec(reation|)\s*-?\s*(centers?)*')

combine_keywords_in_keyword_json_dict(keyword_json_dict, ['School', 'Schools'], 'School', r'schools?')

'''

Refine regular expressions

'''

refined_regexs = {
    'Tracts' : r'tracts?',
    'High Schools' : r'high\s*-?\s*schools?'
}

for key in refined_regexs:
    normalized_key = normalize_keyword(key)
    keyword_json_dict[normalized_key]['regExpr'] = refined_regexs[normalized_key]

'''

Dump the resulting json

'''
def dump_json(filepath, json_data):
    if not os.path.exists(os.path.dirname(filepath)): # create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath))

    with open(filepath, 'w') as file:
        file.write('app.cfg.RESPONSE_MAP = ')
        file.write(json.dumps(json_data, indent=4))
workspace = os.path.dirname(os.path.abspath(__file__))
json_file_path = workspace + r'/keywordData.js'

dump_json(json_file_path, keyword_json_dict)

'''

To-Do:

Regular expressions that need fixing:

boundary / boundaries
high schools?
youth centers


'''