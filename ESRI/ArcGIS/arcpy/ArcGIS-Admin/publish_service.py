# publish service from a ArcGIS Pro Project file (aprx)

import arcpy, os, sys

workspace = os.path.dirname(os.path.abspath(__file__))

# Set output file names
outdir = workspace
service_name = 'GEOGRAPHIES_2'
sddraft_filename = service_name + '.sddraft'
sddraft_output_filename = os.path.join(outdir, sddraft_filename)
sd_filename = service_name + '.sd'
sd_output_filename = os.path.join(outdir, sd_filename)

# Reference map to publish
aprx_path = r'C:\Users\user\Documents\Github\Atlas\src\aprx\TEST\GEOGRAPHIES\GEOGRAPHIES.aprx'
aprx = arcpy.mp.ArcGISProject(aprx_path)

m = aprx.listMaps()[0]

# Create MapServiceDraft and set metadata and server folder properties
target_server_connection = r'C:\Users\user\Documents\Github\Atlas\src\aprx\TEST\CONN\arcgis on localhost_6443.ags' # note that this connection file was created manually by creating a pro project and adding a arcgis server connection
sddraft = arcpy.sharing.CreateSharingDraft('STANDALONE_SERVER', 'MAP_SERVICE', service_name, m)
sddraft.targetServer = target_server_connection
sddraft.credits = ''
sddraft.description = ''
sddraft.summary = 'a'
sddraft.tags = 'a'
sddraft.useLimitations = ''
sddraft.serverFolder = 'ATLAS'

# Create Service Definition Draft file
sddraft.exportToSDDraft(sddraft_output_filename)

# Stage Service
print('Start Staging')
arcpy.server.StageService(sddraft_output_filename, sd_output_filename)

# Publish to server
print('Start Uploading')
arcpy.server.UploadServiceDefinition(sd_output_filename, target_server_connection)

print('Finish Publishing')

# clean up publish files
try:
    os.remove(os.path.join(outdir, sddraft_filename))
    os.remove(os.path.join(outdir, sd_filename))
    os.remove(os.path.join(outdir, 'Thumbnail.png'))
except OSError:
    pass