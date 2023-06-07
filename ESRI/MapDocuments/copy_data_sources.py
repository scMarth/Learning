import arcpy, os, sys, shutil

def error_exit(msg):
    print(msg)
    sys.exit()

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

workspace = os.path.dirname(os.path.abspath(__file__))

# select one mxd folder to copy from
copy_from = [
    # 'DEV',
    # 'TEST',
    'STAGE',
    # 'UAT',
    # 'PROD'
]

# set path to store the output mxds
output_path = workspace + r'\copied_mxds'

if not os.path.exists(output_path):
    os.mkdir(output_path)

if len(copy_from) != 1:
    error_exit('Please select only 1 environment.')

files = os.listdir(workspace + r'\..\{}'.format(copy_from[0]))

for file in files:

    if file.endswith('.mxd'):

        mxd_path = os.path.abspath(workspace + r'\..\{}\{}'.format(copy_from[0], file))
        output_mxd_path = output_path + r'\{}'.format(file)

        shutil.copy(mxd_path, output_mxd_path)

        print(output_mxd_path)

        mxd = arcpy.mapping.MapDocument(output_mxd_path)

        print('\tlayers:')
        for lyr in arcpy.mapping.ListLayers(mxd):
            print('\t\t{}'.format(lyr.name))

            if lyr.name == 'TRANSACTIONAL RANCH NUMBERS' and file == 'SUPPORT.mxd':
                print('\t\t(skipping)')
                # for this layer in SUPPORT.mxd, the source is a Query Feature Class, skip it
                continue
            else:

                # get the current data source and other properties
                current_ds = lyr.dataSource
                print('\t\told data source: {}'.format(current_ds))

                current_table = current_ds.split('.sde\\')[1]
                new_ds = connection.split('\\PROD_DATASTORE_01.AWS')[0]

                print('\t\tnew data source: {}'.format(new_ds))

                # if lyr.supports("DATASETNAME"):
                    # print("datasetName: {}".format(lyr.datasetName))

                # connection = r"D:\DatabaseConnection\PROD_DATASTORE_01.sde\PROD_DATASTORE_01.AWS."

                lyr.replaceDataSource(new_ds, 'SDE_WORKSPACE', lyr.datasetName, False)
                print('')
    
        print('\ttables views:')
        for tbl in arcpy.mapping.ListTableViews(mxd):
            print('\t\t{}'.format(tbl.name))

            current_ds = tbl.dataSource
            # get the current data source and other properties
            print('\t\told data source: {}'.format(current_ds))

            current_table = current_ds.split('.sde\\')[1]
            new_ds = connection.split('\\PROD_DATASTORE_01.AWS')[0]
            
            print('\t\tnew data source: {}'.format(new_ds))

            tbl.replaceDataSource(new_ds, 'SDE_WORKSPACE', tbl.datasetName, False)
            print('')

        print('')


        mxd.save()
        del mxd
        # sys.exit()