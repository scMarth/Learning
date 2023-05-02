import arcpy, os, sys

def error_exit(msg):
    print(msg)
    sys.exit()

workspace = os.path.dirname(os.path.abspath(__file__))

# select one mxd folder to copy from
copy_from = [
    'DEV',
    # 'TEST',
    # 'STAGE',
    # 'UAT',
    # 'PROD'
]


# set up for environment
environment = os.environ["DATASTORE_ENVIRONMENT"]
gdb_number = os.environ["DATASTORE_GDB_NUMBER"]

if environment == "DEV":
    connection = r"D:\DatabaseConnection\DEV_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "TEST":
    connection = r"D:\DatabaseConnection\TEST_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "UAT":
    connection = r"D:\DatabaseConnection\UAT_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "STAGE" or environment == "STG" or environment == "STAGING":
    connection = r"D:\DatabaseConnection\STAGE_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "PROD" or "Prod":
    connection = r"D:\DatabaseConnection\PROD_DATASTORE_01.sde\PROD_DATASTORE_01.AWS."





# sanity check

# trn_v = r"D:/DatabaseConnection/DEV_DATASTORE_03.sde/PROD_DATASTORE_01.aws.TRANSACTIONAL_RANCH_NUMBERS_V"
# with arcpy.da.SearchCursor(trn_v, '*') as sc: # this works
#     for row in sc:
#         print(row)

# desc = arcpy.Describe(trn_v) # this says that trn_v DNE...


# root_directory = r".."
root_directory = connection.split(r'\PROD_DATASTORE_01')[0]
print(root_directory)

arcpy.env.workspace = root_directory

featureclasses = arcpy.ListFeatureClasses()
for featureclass in featureclasses:
    # print(featureclass)

    for view_name in ['RPT_TRANSACTIONAL_RANCH_NUMBERS_V']:
        if featureclass.split('.')[-1] == view_name:

            print(featureclass)
            desc = arcpy.Describe(connection.split('.AWS')[0] + featureclass.split('PROD_DATASTORE_01')[1])
            print(desc.name)
            print(desc.dataType)
            print(desc.datasetType)
            # print(desc.connectionProperties) # DNE
            # print(desc)
sys.exit()

if len(copy_from) != 1:
    error_exit('Please select only 1 environment.')

files = os.listdir(workspace + r'\..\{}'.format(copy_from[0]))

for file in files:

    if file.endswith('.mxd'):
        mxd_path = os.path.abspath(workspace + r'\..\{}\{}'.format(copy_from[0], file))

        print(mxd_path)

        mxd = arcpy.mapping.MapDocument(mxd_path)

        for lyr in arcpy.mapping.ListLayers(mxd):

            print(lyr.name)
            print(lyr.longName)
            print(lyr.dataSource)

            print('data source: ' + lyr.dataSource)
            
            desc = arcpy.Describe(lyr.dataSource)
            print('desc created')
            print(dir(desc))
            print('desc:')
            print(desc.workspaceType)
            print(desc.datasetName)
            print(desc.isFeatureClassRelative)



            print('\n')

        print('\n')
        del mxd