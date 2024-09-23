import arcpy, json, shutil, os, re
from arcgis.gis import GIS


# Variables
sourcePortal = arcpy.GetParameterAsText(0)
sourceIWA = arcpy.GetParameterAsText(1)
sourceUsername = arcpy.GetParameterAsText(2)
sourcePassword = arcpy.GetParameterAsText(3)
sourceUser = arcpy.GetParameterAsText(4)
content = arcpy.GetParameterAsText(5)
webMaps = arcpy.GetParameterAsText(6)
standaloneLayers = arcpy.GetParameterAsText(7)
targetPortal = arcpy.GetParameterAsText(8)
targetIWA = arcpy.GetParameterAsText(9)
targetUsername = arcpy.GetParameterAsText(10)
targetPassword = arcpy.GetParameterAsText(11)
targetOwner = arcpy.GetParameterAsText(12)
targetFolder = arcpy.GetParameterAsText(13)
scratchFolder = arcpy.env.scratchFolder

# Function to update thumbnail
def updateThumbnail(previousItem, newItem):
    '''Function to update the web map/apps thumbnail'''
    thumbNail = previousItem.download_thumbnail(scratchFolder)
    if thumbNail:
        newItem.update(thumbnail=thumbNail)
        os.remove(thumbNail)

# Funtion to clear scratch workspace
def clearScratchWorkspace():
    '''Function will remove all contents from scratch workspace'''

    arcpy.AddMessage("Cleaning up scratch workspace")
    shutil.rmtree(scratchFolder)

# Sign into source portal
arcpy.AddMessage("Signing into source portal")
source = GIS(sourcePortal, sourceUsername, sourcePassword, verify_cert=False)

# Sign into target portal
arcpy.AddMessage("Signing into target portal")
target = GIS(targetPortal, targetUsername, targetPassword, verify_cert=False)

# Get Dashboard ID
arcpy.AddMessage("Getting Dashboard ID")
dashboardID = content.split(' - ')[-1]
appTitle = source.content.get(dashboardID).title

# Get Dashboard JSON
arcpy.AddMessage("Getting Dashboard JSON")
dashboardApp = source.content.get(dashboardID)
dashboardAppDict = dashboardApp.get_data(try_json=True)

# Convert dict to JSON
arcpy.AddMessage("Converting dict to JSON")
dashboardAppJSON = json.dumps(dashboardAppDict)

# Replace web maps
arcpy.AddMessage("Replacing Web Maps and Stand-alone Layers")
webMapIdList = webMaps.split(';')
standaloneLayersList = standaloneLayers.split(';')

replacementLists = []
if len(webMapIdList) == 1:
    if webMapIdList[0] != '':
        replacementLists.append(webMapIdList)
elif len(webMapIdList) > 1:
    replacementLists.append(webMapIdList)
if len(standaloneLayersList) > 0 and len(standaloneLayersList) < 2:
    if len(standaloneLayersList) == 1:
        if standaloneLayersList[0] != '':
            replacementLists.append(standaloneLayersList)
elif len(standaloneLayersList) > 1:
    replacementLists.append(standaloneLayersList)

for replacementList in replacementLists:
    x = 0
    while x < len(replacementList):
        webMap1 = replacementList[x].split(" ")[0]
        webMap2 = replacementList[x].split(" ")[1]
        dashboardAppJSON = dashboardAppJSON.replace(webMap1, webMap2)
        x += 1

# Replace portalUrl
compiled = re.compile(re.escape(sourcePortal), re.IGNORECASE)
dashboardAppJSON = compiled.sub(targetPortal, dashboardAppJSON)
# dashboardAppJSON = dashboardAppJSON.replace(sourcePortal, targetPortal)

# Check if Dashboard exists
exists = False
for result in target.content.search(f"title:{appTitle} AND owner:{targetOwner}", item_type='Dashboard'):
   if result['title'] == appTitle:
       dashboardApp2 = result
       exists = True

# Create a copy of Dashboard/update existing Dashboard
dashboard_app_properties = {'title': dashboardApp.title,
                      'type': 'Dashboard',
                      'snippet': dashboardApp.snippet,
                      'description': dashboardApp.description,
                      'tags': dashboardApp.tags,
                      'typeKeywords': "ArcGIS Dashboards, Dashboard, Operations Dashboard",
                      'text': dashboardAppJSON}

if exists == False:
    arcpy.AddMessage("Creating a copy of the Dashboard")
    if targetFolder == 'ROOT':
        dashboardAppItem = target.content.add(item_properties=dashboard_app_properties, owner=targetOwner)
    else:
        dashboardAppItem = target.content.add(item_properties=dashboard_app_properties, owner=targetOwner, folder=targetFolder)
elif exists == True:
    arcpy.AddMessage(f"Updating existing Dashboard {dashboardApp2.title}")
    dashboardApp2.update(item_properties=dashboard_app_properties)
    dashboardAppItem = dashboardApp2


# Update Thumbnail
arcpy.AddMessage("Updating thumbnail")
updateThumbnail(dashboardApp, dashboardAppItem)

# Call function to clear scratch workspace
clearScratchWorkspace()
