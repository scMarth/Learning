import csv, sys, arcpy, datetime, os, shutil, re

from street_suffix_abbreviations import cast_street_suffixes_to_abrs

start_time = datetime.datetime.now()
print('Start: {}'.format(start_time))

# read unknown addresses into memory
unknowns_hash = {} # mapping from object id to the address point record
fc = r'\server\test.gdb\unknowns'
with arcpy.da.SearchCursor(fc, ['*', 'SHAPE@']) as cursor:
    for row in cursor:
        objid = row[0]
        unknowns_hash[objid] = row

# read school sites into memory
school_sites = {} # mapping from full addr to the school site record
fc = r'\serverdata\GeoDatabases\Schools.gdb\School_Sites'
with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        full_addr = cast_street_suffixes_to_abrs(row[3].upper())
        # print(full_addr)
        school_sites[full_addr] = row

# read church sites into memory
churches = {} # mapping from full addr to the school site record
fc = r'\serverdata\GeoDatabases\Churches.gdb\City_Churches'
with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        full_addr = cast_street_suffixes_to_abrs(row[3].upper())
        # print(full_addr)
        churches[full_addr] = row

# read hospital sites into memory
hospitals = {} # mapping from full addr to the school site record
fc = r'\serverdata\GeoDatabases\Healthcare.gdb\Hospital'
with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        full_addr = cast_street_suffixes_to_abrs(row[8].upper())
        # print(full_addr)
        hospitals[full_addr] = row

# read commercial zoning data into memory
zoning_data = {}
fc = r'\serverdata\GeoDatabases\Zoning.gdb\Zoning\zoning_polygon'
with arcpy.da.SearchCursor(fc, ['*', "SHAPE@"]) as cursor:
    for row in cursor:
        # print(row)
        zoning_district = row[13]

        '''

        store all polygons that are of type

            commercial
            industrial
            semipublic
            agricultural
            parks

        into zoning_data. Later, a point will be tested against all the remaining polygons. Any point
        in any of the polygons will be ignored and not added to the fc.

        '''
        if not re.search('COMMERCIAL', zoning_district.upper()) \
        and not re.search('INDUSTRIAL', zoning_district.upper()) \
        and not re.search('SEMIPUBLIC', zoning_district.upper()) \
        and not re.search('AGRICULTURAL', zoning_district.upper()) \
        and not re.search('PARKS', zoning_district.upper()):
            continue

        # print(zoning_district)
        # print(row[12]) # should be the polygon
        objid = row[0]
        # print(row[12])
        zoning_data[objid] = row

# dump 
fields = [ \
    'SHAPE@XY', \
    'HOUSENUMBER', \
    'STREETNAME', \
    'APARTMENT_UNIT', \
    'ZIP', \
    'GQ_TL_NAME', \
    'FACILITY_NAME', \
    'LOCATION_DESCRIPTION', \
    'NONCITYSTYLE_ADDRESS', \
    'NONCITYSTYLE_ZIP', \
    'MAPSPOT', \
    'LAT', \
    'LONG', \
    'CITY_STYLE' \
]

spatial_reference = arcpy.SpatialReference(102644) # WKID for NAD 1983

basepath = r'\server\folder'
fgdb_path = basepath + r'\test.gdb'

arcpy.env.workspace = fgdb_path

fc = fgdb_path + r'\residential_mixed_and_open_spaces'

if arcpy.Exists(fc):
    # arcpy.DeleteFeatures_management(fc) # doesn't delete the actual feature class
    arcpy.Delete_management(fc)

arcpy.CreateFeatureclass_management(out_path=fgdb_path, out_name='residential_mixed_and_open_spaces', geometry_type='POINT', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_reference)

# add attributes to the newly created feature class
arcpy.AddField_management('residential_mixed_and_open_spaces', 'HOUSENUMBER', 'TEXT', field_alias='HOUSENUMBER', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'STREETNAME', 'TEXT', field_alias='STREETNAME', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'APARTMENT_UNIT', 'TEXT', field_alias='APARTMENT_UNIT', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'ZIP', 'TEXT', field_alias='ZIP', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'GQ_TL_NAME', 'TEXT', field_alias='GQ_TL_NAME', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'FACILITY_NAME', 'TEXT', field_alias='FACILITY_NAME', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'LOCATION_DESCRIPTION', 'TEXT', field_alias='LOCATION_DESCRIPTION', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'NONCITYSTYLE_ADDRESS', 'TEXT', field_alias='NONCITYSTYLE_ADDRESS', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'NONCITYSTYLE_ZIP', 'TEXT', field_alias='NONCITYSTYLE_ZIP', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'MAPSPOT', 'TEXT', field_alias='MAPSPOT', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'LAT', 'TEXT', field_alias='LAT', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'LONG', 'TEXT', field_alias='LONG', field_is_nullable='NULLABLE')
arcpy.AddField_management('residential_mixed_and_open_spaces', 'CITY_STYLE', 'TEXT', field_alias='CITY_STYLE', field_is_nullable='NULLABLE')

def convert_4269_to_102644(longitude, latitude):
    point = arcpy.Point(longitude, latitude)
    sr = arcpy.SpatialReference(4269) # WGS84
    point_geometry = arcpy.PointGeometry(point, sr)

    target_spatial_ref = arcpy.SpatialReference(102644) # NAD83
    projected = point_geometry.projectAs(target_spatial_ref)

    return [projected.firstPoint.X, projected.firstPoint.Y]

unknowns_count = 0
leftovers = 0
leftovers_not_in_commercial_zones = 0

with arcpy.da.InsertCursor(fc, fields) as cursor:
    for objid in unknowns_hash:
        record = unknowns_hash[objid]
        # print(record)
        house_number = record[14]
        street_name = record[15]
        suite_apt = record[16]

        # print(record)
        # sys.exit()

        point = record[-1]

        full_addr = house_number + ' ' + street_name + ' ' + suite_apt

        full_addr = cast_street_suffixes_to_abrs(full_addr.upper())

        unknowns_count += 1

        if (full_addr not in hospitals) and (full_addr not in churches) and (full_addr not in school_sites):
            leftovers += 1

            in_zoning = False

            for objid in zoning_data:
                zoning_record = zoning_data[objid]
                polygon = zoning_record[-1]

                if polygon.contains(point):
                    in_zoning = True

            if not in_zoning:
                leftovers_not_in_commercial_zones += 1

                x = None
                y = None

                try:
                    x = float(record[-4])
                    y = float(record[-5])
                except:
                    x = 0
                    y = 0

                x, y = convert_4269_to_102644(x, y)

                xy = (x,y)

                cursor.insertRow(( \
                    xy, \
                    record[14], \
                    record[15], \
                    record[16], \
                    record[17], \
                    record[18], \
                    record[19], \
                    record[20], \
                    record[21], \
                    record[22], \
                    record[23], \
                    record[24], \
                    record[25], \
                    record[26] \
                ))

print('unknowns_count = {}'.format(unknowns_count))
print('leftovers = {}'.format(leftovers))
print('leftovers_not_in_commercial_zones = {}'.format(leftovers_not_in_commercial_zones))

end_time = datetime.datetime.now()
print('')
print('End: {}'.format(end_time))
print('')
print('Duration: {}'.format(end_time - start_time))