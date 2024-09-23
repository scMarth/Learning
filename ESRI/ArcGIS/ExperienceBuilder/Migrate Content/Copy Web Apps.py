import arcpy, json, shutil, os, re
from arcgis.gis import GIS


# Variables
sourcePortal = arcpy.GetParameterAsText(0)
sourceIWA = arcpy.GetParameterAsText(1)
sourceUsername = arcpy.GetParameterAsText(2)
sourcePassword = arcpy.GetParameterAsText(3)
sourceUser = arcpy.GetParameterAsText(4)
content = arcpy.GetParameterAsText(5)
operationalLayers = arcpy.GetParameterAsText(6)
targetPortal = arcpy.GetParameterAsText(7)
targetIWA = arcpy.GetParameterAsText(8)
targetUsername = arcpy.GetParameterAsText(9)
targetPassword = arcpy.GetParameterAsText(10)
targetOwner = arcpy.GetParameterAsText(11)
targetFolder = arcpy.GetParameterAsText(12)
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

# Get Web App ID
arcpy.AddMessage("Getting Web App ID")
webAppID = content.split(' - ')[-1]
appTitle = source.content.get(webAppID).title

# Get Web App JSON
arcpy.AddMessage("Getting Web Map JSON")
webApp = source.content.get(webAppID)
webAppDict = webApp.get_data(try_json=True)

# Convert dict to JSON
arcpy.AddMessage("Converting dict to JSON")
webAppJSON = json.dumps(webAppDict)

# Replace web maps
arcpy.AddMessage("Replacing Web Maps")
x = 0
webmaps = operationalLayers.split(';')
while x < len(webmaps):
    webmap1 = webmaps[x].split(" ")[0]
    webmap2 = webmaps[x].split(" ")[1]
    webAppJSON = webAppJSON.replace(webmap1, webmap2)
    x += 1

# Replace portalUrl
compiled = re.compile(re.escape(sourcePortal), re.IGNORECASE)
webAppJSON = compiled.sub(targetPortal, webAppJSON)
# webAppJSON = webAppJSON.replace(sourcePortal, targetPortal)

# Check if web app exists
exists = False
for result in target.content.search(f"title:{appTitle} AND owner:{targetOwner}", item_type='Web Mapping Application'):
   if result['title'] == appTitle:
       webApp2 = result
       exists = True

# Create a copy of web app/update existing web app
if 'configurableApp' in webApp.typeKeywords:
    typeKeywords = "configurableApp, JavaScript, Map, Mapping Site, Online Map, Ready To Use, Web Map"
else:
    typeKeywords = "JavaScript,Map,Mapping Site,Online Map,Ready To Use,WAB2D,Web AppBuilder,Web Map"
wab_app_properties = {'title': webApp.title,
                      'type': 'Web Mapping Application',
                      'snippet': webApp.snippet,
                      'description': webApp.description,
                      'tags': webApp.tags,
                      'typeKeywords': typeKeywords,
                      'text': webAppJSON}

if exists == False:
    arcpy.AddMessage("Creating a copy of the web app")
    if targetFolder == 'ROOT':
        webAppItem = target.content.add(item_properties=wab_app_properties, owner=targetOwner)
    else:
        webAppItem = target.content.add(item_properties=wab_app_properties, owner=targetOwner, folder=targetFolder)
elif exists == True:
    arcpy.AddMessage(f"Updating existing web app {webApp2.title}")
    webApp2.update(item_properties=wab_app_properties)
    webAppItem = webApp2

# Update web app id
if exists == False:
    arcpy.AddMessage("Updating web app ID and URL")
    webAppID2 = webAppItem.id
    webAppJSON = webAppJSON.replace(webAppID, webAppID2)
    url = webApp.url
    url = url.replace(webAppID, webAppID2)
    url = url.replace(sourcePortal, targetPortal)
    wab_app_properties = {'url': url, 'text': webAppJSON}
    webAppItem.update(item_properties=wab_app_properties)


# Update Thumbnail
arcpy.AddMessage("Updating thumbnail")
updateThumbnail(webApp, webAppItem)

# Call function to clear scratch workspace
clearScratchWorkspace()
