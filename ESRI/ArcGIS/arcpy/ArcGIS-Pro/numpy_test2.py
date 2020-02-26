import arcpy, os, shutil, numpy

def createTestFGDB():
    basepath = r'.'
    fgdb_path = basepath + r'\testPoints.gdb'

    # if the file geodatabase exists, delete it
    if os.path.exists(fgdb_path):
        shutil.rmtree(fgdb_path)

    # create fgdb
    arcpy.CreateFileGDB_management(basepath, 'testPoints')

    # create a new feature class
    arcpy.CreateFeatureclass_management(out_path=fgdb_path, out_name='testPoints', geometry_type='POINT', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=None)

    arcpy.env.workspace = fgdb_path

    # add attributes to the newly created feature class
    # NOTE: OBJECTID is added for you
    arcpy.AddField_management('testPoints', 'First_Name', 'TEXT', field_alias='First Name', field_is_nullable='NULLABLE')
    arcpy.AddField_management('testPoints', 'Last_Name', 'TEXT', field_alias='Last Name', field_is_nullable='NULLABLE')

    fc = fgdb_path + r'\testPoints'

    fields = [ \
        'SHAPE@XY', \
        'First_Name', \
        'Last_Name' \
    ]

    x = 0
    y = 0

    data = [ \
        ['Bob', 'Dole'], \
        ['Crash', 'Bandicoot'], \
        ['Coco', 'Bandicoot'] \
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

basepath = r'.'
fgdb_path = basepath + r'\testPoints.gdb'
fc = fgdb_path + r'\testPoints'

npa = arcpy.da.TableToNumPyArray(fc, field_names='*') # use '*' to get all fields
print(npa)
print("")

print(npa['First_Name'])
print("")

print(npa.dtype.names) # print column names
print("")
# print(npa.dtype) # not very useful

print(npa[1])
print("")

print(npa[npa.dtype.names[0]]) # first fields
print(npa[npa.dtype.names[1]]) # second fields
print(npa[npa.dtype.names[2]]) # third fields
print(npa[npa.dtype.names[3]]) # forth fields