'''
try to catch exceptions for inserting data with emojis into a fgdb
'''

import arcpy, os, shutil

workspace =  os.path.dirname(os.path.abspath(__file__))

# create a test fgdb
fgdb_path = workspace + '\emojiTest.gdb'

if os.path.exists(fgdb_path):
    shutil.rmtree(fgdb_path)

# create fgdb
arcpy.CreateFileGDB_management(workspace, 'emojiTest')

rf = arcpy.SpatialReference(102644)

# create a new feature class
arcpy.CreateFeatureclass_management(out_path=fgdb_path, out_name='emojiTest', geometry_type='POINT', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=rf)

arcpy.env.workspace = fgdb_path

# add attributes to the newly created feature class
# NOTE: OBJECTID is added for you
arcpy.AddField_management('emojiTest', 'First_Name', 'TEXT', field_alias='First Name', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Last_Name', 'TEXT', field_alias='Last Name', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Favorite_Color1', 'TEXT', field_alias='Favorite Color 1', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Favorite_Color2', 'TEXT', field_alias='Favorite Color 2', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Favorite_Color3', 'TEXT', field_alias='Favorite Color 3', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Favorite_Color4', 'TEXT', field_alias='Favorite Color 4', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Favorite_Color5', 'TEXT', field_alias='Favorite Color 5', field_is_nullable='NULLABLE')
arcpy.AddField_management('emojiTest', 'Favorite_Color6', 'TEXT', field_alias='Favorite Color 6', field_is_nullable='NULLABLE')

fc = fgdb_path + r'\emojiTest'

fields = [ \
    'SHAPE@XY', \
    'First_Name', \
    'Last_Name', \
    'Favorite_Color1', \
    'Favorite_Color2', \
    'Favorite_Color3', \
    'Favorite_Color4', \
    'Favorite_Color5', \
    'Favorite_Color6', \
]

x = 0
y = 0

# data with emoji fails, ones without work
data = [ \
    ['Bob', 'Dole', 'red', 'red', 'red', 'red', 'red', 'red'], \
    ['Crash', 'Bandicoot', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'], \
    ['Coco', 'my poor dogs 🐕😳', 'pink', 'pink', 'pink', 'pink', 'pink', 'pink'], \
    ['Tiny', 'Tiger', 'green', 'green', 'green', 'green', 'green', 'green'] \
    # ['Coco', 'my poor dogs '] \
]

with arcpy.da.InsertCursor(fc, fields) as cursor:
    for record in data:
        x += 1
        y += 1
        xy = (x,y)
        try:
            cursor.insertRow(( \
                xy, \
                record[0], \
                record[1], \
                record[2], \
                record[3], \
                record[4], \
                record[5], \
                record[6], \
                record[7] \
            ))
        except:
            print('EXCEPTION ON insertRow:')
            print(record)
            continue

print('\nPrinting contents of feature class:\n')

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print(row)

'''
insertRow seems to just write everything except the emoji field anyways
'''
        
