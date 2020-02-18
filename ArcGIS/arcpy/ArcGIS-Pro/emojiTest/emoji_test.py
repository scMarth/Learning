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

fc = fgdb_path + r'\emojiTest'

fields = [ \
    'SHAPE@XY', \
    'First_Name', \
    'Last_Name' \
]

x = 0
y = 0

# data with emoji fails, ones without work
data = [ \
    ['Bob', 'Dole'], \
    ['Crash', 'Bandicoot'], \
    # ['Coco', 'my poor dogs 🐕😳'] \
    ['Coco', 'my poor dogs '] \
]

with arcpy.da.InsertCursor(fc, fields) as cursor:
    for record in data:
        x += 1
        y += 1
        xy = (x,y)
        cursor.insertRow(( \
            xy, \
            record[0], \
            record[1] \
        ))
