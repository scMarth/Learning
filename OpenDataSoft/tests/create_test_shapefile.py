import arcpy, os, shutil, numpy

def createTestShapefile():
    basepath = os.path.dirname(__file__)
    shp_path = basepath + r'\testPoints'

    # if the file geodatabase exists, delete it
    if os.path.exists(shp_path):
        shutil.rmtree(shp_path)

    os.mkdir(shp_path)

    # create fgdb
    # arcpy.CreateFileGDB_management(basepath, 'testPoints')

    spatial_ref = arcpy.SpatialReference(102644) # NAD83

    # create a new feature class
    arcpy.CreateFeatureclass_management(out_path=shp_path, out_name='testPoints', geometry_type='POINT', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_ref)

    arcpy.env.workspace = shp_path

    # add attributes to the newly created feature class
    # NOTE: OBJECTID is added for you

    print('Adding fields...')

    arcpy.AddField_management('testPoints.shp', 'Text', 'TEXT', field_alias='Text', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints.shp', 'Integer', 'TEXT', field_alias='Integer', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints.shp', 'Decimal', 'TEXT', field_alias='Decimal', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints.shp', 'Datetime', 'TEXT', field_alias='Datetime', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints.shp', 'Date_Year', 'TEXT', field_alias='Date_Year', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints.shp', 'Date_Month', 'TEXT', field_alias='Date_Month', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints.shp', 'Date_Day', 'TEXT', field_alias='Date_Day', field_is_nullable='NULLABLE')

    print('Inserting data...')

    fc = shp_path + r'\testPoints.shp'

    fields = [ \
        'SHAPE@XY', \
        'Text', \
        'Integer', \
        'Decimal', \
        'Datetime', \
        'Date_Year', \
        'Date_Month', \
        'Date_Day' \
    ]

    x = 5784181.434937561
    y = 2139043.6504749693

    data = [ \
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['lnnn', '8', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bnnnnnob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bbhob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bhjghghob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bggyob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Buiouioob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        ['1', 'asdf', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # causes Integer error
        ['1', '1 + 1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # causes Integer error
        ['1.5', '324.222', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # OK, decimal is truncated (LOSS OF DATA)
        ['2', '8', '1.043fds', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # causes Decimal error
        ['3', '8', '1', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # OK (putting int in decimal field)
        ['4', '8', '1.043', '13/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # OK, swaps month and date (POTENTIALLY WRONG)
        ['4.5', '8', '1.043', '13/13/2019 12:24 PM', '2019', '11/2019', '11/6/2019'], # error because can't interpret 13/13 for month / day (both options exceed 12 months)
        ['5', '8', '1.043', '13/6/2019 14:24', '2019', '11/2019', '11/6/2019'],  # OK 7:24 AM ...????? it subtracted  7... (WRONG)
        ['6', '8', '1.043', '13/6/2019', '2019', '11/2019', '11/6/2019'],  # OK ... June 12, 2019 5:00 PM (WRONG?)
        ['7', '8', '1.043', '11/6/2019 12:24 PM', 'asdf', '11/2019', '11/6/2019'], # causes Date Year error
        ['8', '8', '1.043', '11/6/2019 12:24 PM', '2019', '11', '11/6/2019'], # OK January 2001 (WRONG?? .. Potential data corruption)
        ['8.25', '8', '1.043', '11/6/2019 12:24 PM', '2019', '13/2019', '11/6/2019'], # Can't convert into a date error
        ['8.35', '8', '1.043', '11/6/2019 12:24 PM', '2019', 'January 2019', '11/6/2019'], # OK January 2019
        ['8.45', '8', '1.043', '11/6/2019 12:24 PM', '2019', 'Jan. 2019', '11/6/2019'], # OK November 2019 (WRONG)
        ['8.5', '8', '1.043', '11/6/2019 12:24 PM', '2019', 'asdf', '11/6/2019'], # date_month error
        ['9', '8', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '2019'], # OK January 1, 2019 (WRONG)
        ['9.5', '8', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', 'asdfadsf'], # date_day error
        ['Bob', '1', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019'],
        # testing UNIX timestamps
        ['Bob', '20', '1.043', '1521244800000', '2019', '11/2019', '11/6/2019'], # seconds
        ['Bob', '19', '1.043', '1521244800', '2019', '11/2019', '11/6/2019'], # milliseconds
        ['Bob', '18', '1.043', 'March 17, 2018 12:00:00 AM', '2019', '11/2019', '11/6/2019'], # string
        ['Bob', '19852347825', '1.043', '11/6/2019 12:24 PM', '2019', '11/2019', '11/6/2019']
    ]

    with arcpy.da.InsertCursor(fc, fields) as cursor:
        for record in data:
            xy = (x,y)

            insert = [xy]

            for field in record:
                insert.append(field)

            cursor.insertRow(insert)

createTestShapefile()
print('Done.')

'''

Type definitions:

https://help.opendatasoft.com/platform/en/publishing_data/05_processing_data/defining_a_dataset_schema.html#choosingtype

Looks like any geospatial data is converted into WGS84. Could be why some polygons that look fine in ArcPro can cause processing errors when uploaded to OpenDataSoft portals.

'''