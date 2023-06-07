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

if len(copy_from) != 1:
    error_exit('Please select only 1 environment.')

files = os.listdir(workspace + r'\..\{}'.format(copy_from[0]))

with open(workspace + r'\print_data_sources_output.txt', 'w') as logfile:

    for file in files:

        if file.endswith('.mxd'):
            mxd_path = os.path.abspath(workspace + r'\..\{}\{}'.format(copy_from[0], file))

            logfile.write(mxd_path + '\n')

            mxd = arcpy.mapping.MapDocument(mxd_path)

            for lyr in arcpy.mapping.ListLayers(mxd):

                logfile.write('\t' + lyr.name + '\n')
                logfile.write('\t' + lyr.longName + '\n')
                logfile.write('\t' + lyr.dataSource + '\n')

                print('data source: ' + lyr.dataSource)
                
                desc = arcpy.Describe(lyr.dataSource)
                print('desc created')
                print(dir(desc))
                logfile.write('\t' + 'desc:' + '\n')
                logfile.write('\t\t' + desc.workspaceType + '\n')
                logfile.write('\t\t' + desc.datasetName + '\n')
                logfile.write('\t\t' + desc.isFeatureClassRelative + '\n')



                logfile.write('\n')

            logfile.write('\n')
            del mxd