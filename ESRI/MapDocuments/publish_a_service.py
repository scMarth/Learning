import arcpy, sys, os

# set the path to the map document
mxd_path = r"C:\Users\DevUser\Documents\Github\MyProject\src\mxd\scripting\copied_mxds\GEOGRAPHIES.mxd"

# server_url = "https://<servername>/<instance>/admin"
server_url = "https://localhost:6443/arcgis/admin"
user_name = os.environ["MyProject_USERNAME"]
password = os.environ["MyProject_PASSWORD"]
service_folder = os.environ["MyProject_SERVICE_FOLDER"]

msd_path = mxd_path.replace('.mxd', '.msd')
sddraft_path = mxd_path.replace('.mxd', '.sddraft')
sd_path = mxd_path.replace('.mxd', '.sd')
ags_folder = mxd_path.replace('\\GEOGRAPHIES.mxd', '')
# ags_folder = 'GIS Servers'
ags_filename = 'publish_service_connectionfile.ags'
# print(ags_folder)
# sys.exit()
connection_file_path = os.path.join(ags_folder, ags_filename)

# delete files if they exist
for filepath in [msd_path, sddraft_path, sd_path, connection_file_path]:
    if os.path.exists(filepath):
        os.remove(filepath)

service_name = mxd_path.split('\\')[-1].split('.')[0] + "2"
print(service_name)

folder_name = service_folder

# convert mxd to msd
mxd = arcpy.mapping.MapDocument(mxd_path)
arcpy.mapping.ConvertToMSD(mxd, msd_path)
del mxd

arcpy.mapping.CreateMapSDDraft(msd_path, sddraft_path, service_name, "ARCGIS_SERVER", folder_name=folder_name)

arcpy.StageService_server(sddraft_path, sd_path)


# Create a new server connection file

# arcpy.mapping.CreateGISServerConnectionFile("PUBLISH_GIS_SERVICES", connection_file_path, server_url, "ARCGIS_SERVER", username=user_name, password=password)



arcpy.mapping.CreateGISServerConnectionFile("PUBLISH_GIS_SERVICES", ags_folder, ags_filename, server_url, "ARCGIS_SERVER", username=user_name, password=password)

arcpy.UploadServiceDefinition_server(sd_path, connection_file_path)