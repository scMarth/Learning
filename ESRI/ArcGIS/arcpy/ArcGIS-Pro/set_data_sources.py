'''
Copy the ArcGIS Pro Projects from the envonment specified in "copy_from" into copied_pro_projects, replace the data sources with the correct data sources using the database user, password, and instance for that environment.
'''

import arcpy, os, sys, shutil

def print_and_log(msg):
    print(msg)
    
def error_exit(msg):
    print(msg)
    sys.exit()

# set up for environment
environment = os.environ["APP_ENVIRONMENT"]
gdb_number = os.environ["APP_GDB_NUMBER"]

if environment == "DEV":
    connection = r"D:\DatabaseConnection\DEV_APP_{0}.sde\PROD_APP_01.AWS.".format(gdb_number)
elif environment == "TEST":
    connection = r"D:\DatabaseConnection\TEST_APP_{0}.sde\PROD_APP_01.AWS.".format(gdb_number)
elif environment == "UAT":
    connection = r"D:\DatabaseConnection\UAT_APP_{0}.sde\PROD_APP_01.AWS.".format(gdb_number)
elif environment == "STAGE" or environment == "STG" or environment == "STAGING":
    connection = r"D:\DatabaseConnection\STAGE_APP_{0}.sde\PROD_APP_01.AWS.".format(gdb_number)
elif environment == "PROD" or "Prod":
    connection = r"D:\DatabaseConnection\PROD_APP_01.sde\PROD_APP_01.AWS."

workspace = os.path.dirname(os.path.abspath(__file__))

# select one environment's folder to copy from
copy_from = [
    # 'DEV',
    # 'TEST',
    'TEST2',
    # 'STAGE',
    # 'UAT',
    # 'PROD'
]

# set path to store the output projects
output_path = workspace + r'\copied_pro_projects'

if not os.path.exists(output_path):
    os.mkdir(output_path)

if len(copy_from) != 1:
    error_exit('Please select only 1 environment.')

APP_aprx_folder_names = [
    'GEOGRAPHIES',
    'SUPPORT',
    'WAYLINES'
    # 'WAYLINES_TEST'
]

for project in APP_aprx_folder_names:
    # if project != 'OPERATIONAL_BLACK':
        # continue

    # find the project path
    aprx_folder = os.path.abspath(workspace + r'\..\{}\{}'.format(copy_from[0], project))
    print('input folder: {}'.format(aprx_folder))
    
    # set the location of the output project
    output_aprx_folder = output_path + r'\{}'.format(project)
    print('output folder: {}'.format(output_aprx_folder))

    # remove the destination directory if it exists
    if os.path.exists(output_aprx_folder):
        shutil.rmtree(output_aprx_folder)

    # copy the input project folder
    shutil.copytree(aprx_folder, output_aprx_folder)
    
    output_aprx_path = output_aprx_folder + r'\{}.aprx'.format(project)
    print('output aprx: {}'.format(output_aprx_path))

    aprx = arcpy.mp.ArcGISProject(output_aprx_path)    
    map = aprx.listMaps("Layers")[0]

    print('\tlayers:')
    for lyr in map.listLayers():
        print('\t\t{}'.format(lyr.name))

        if lyr.name == 'TRANSACTIONAL RANCH NUMBERS' and project == 'SUPPORT':
            print('\t\t(skipping)')
            # for this layer in SUPPORT.aprx, the source is a Query Feature Class, skip it
            continue
        else:
            conProp = lyr.connectionProperties

            print('\t\told connection properties:')
            print('\t\t{}'.format(conProp))
            
            conProp['connection_info']['password'] = os.environ['APP_AWS_DB_PASSWORD']
            conProp['connection_info']['user'] = os.environ['APP_AWS_DB_USER']
            conProp['connection_info']['db_connection_properties'] = os.environ['APP_DB_INSTANCE']
            conProp['connection_info']['instance'] = 'sde:sqlserver:{}'.format(os.environ['APP_DB_INSTANCE'])
            conProp['connection_info']['server'] = os.environ['APP_DB_INSTANCE']
            lyr.updateConnectionProperties(lyr.connectionProperties, conProp)

            print('\t\tnew connection properties:')
            print('\t\t{}'.format(lyr.connectionProperties))
            print('')

    print('\ttables:')
    for tbl in map.listTables():
        conProp = tbl.connectionProperties

        print('\t\told connection properties:')
        print('\t\t{}'.format(conProp))

        conProp['connection_info']['password'] = os.environ['APP_AWS_DB_PASSWORD']
        conProp['connection_info']['user'] = os.environ['APP_AWS_DB_USER']
        conProp['connection_info']['db_connection_properties'] = os.environ['APP_DB_INSTANCE']
        conProp['connection_info']['instance'] = 'sde:sqlserver:{}'.format(os.environ['APP_DB_INSTANCE'])
        conProp['connection_info']['server'] = os.environ['APP_DB_INSTANCE']
        tbl.updateConnectionProperties(lyr.connectionProperties, conProp)

        print('\t\tnew connection properties:')
        print('\t\t{}'.format(lyr.connectionProperties))
        print('')

    print('')

    aprx.saveACopy(output_aprx_path)
    del aprx
    sys.exit()
