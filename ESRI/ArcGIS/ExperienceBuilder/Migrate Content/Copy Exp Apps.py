import arcpy, json, os, zipfile, shutil, re
from arcgis.gis import GIS


# Variables
sourcePortal = arcpy.GetParameterAsText(0)
sourceIWA = arcpy.GetParameterAsText(1)
sourceUsername = arcpy.GetParameterAsText(2)
sourcePassword = arcpy.GetParameterAsText(3)
sourceUser = arcpy.GetParameterAsText(4)
content = arcpy.GetParameterAsText(5)
webMaps = arcpy.GetParameterAsText(6)
embeded = arcpy.GetParameterAsText(7)
targetPortal = arcpy.GetParameterAsText(8)
targetIWA = arcpy.GetParameterAsText(9)
targetUsername = arcpy.GetParameterAsText(10)
targetPassword = arcpy.GetParameterAsText(11)
targetOwner = arcpy.GetParameterAsText(12)
targetFolder = arcpy.GetParameterAsText(13)


def downloadExpAppResources(app):
    '''Function to download Experience Builder application resources'''

    # Download Experience Builder App Resources to scratch directory
    arcpy.AddMessage(f"Downloading Resources for {app.title}")
    app.resources.export(scratchFolder, 'Resources.zip')

    # Extract Zipped Resources
    arcpy.AddMessage(f"Extracting Resources for {app.title}")
    with zipfile.ZipFile(os.path.join(scratchFolder, 'Resources.zip'), 'r') as zip_ref:
        zip_ref.extractall(scratchFolder)


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

# # Update source portal to have capital letter
# sourcePortal = sourcePortal.split("://")[0] + '://' + sourcePortal.split("://")[1].capitalize()
# arcpy.AddMessage(sourcePortal)

# Create scratch Directory
scratchFolder = os.path.join(arcpy.env.scratchFolder, 'Resources')
if not os.path.exists(scratchFolder):
    os.mkdir(scratchFolder)

# Get Exp App ID
arcpy.AddMessage("Getting Exp App ID")
expAppID = content.split(' - ')[-1]
appTitle = source.content.get(expAppID).title

# Get Exp App JSON
arcpy.AddMessage("Getting Exp App JSON")
expApp = source.content.get(expAppID)
expAppDict = expApp.get_data(try_json=True)

# Convert dict to JSON
arcpy.AddMessage("Converting dict to JSON")
expAppJSON = json.dumps(expAppDict)

# Replace web maps/embeded URLs
arcpy.AddMessage("Replacing Web Maps/Embedded URLs")
webMapIdList = webMaps.split(';')
embededList = embeded.split(';')

replacementLists = []
if len(webMapIdList) == 1:
    if webMapIdList[0] != '':
        replacementLists.append(webMapIdList)
elif len(webMapIdList) > 1:
    replacementLists.append(webMapIdList)
if len(embededList) > 0 and len(embededList) < 2:
    if len(embededList) == 1:
        if embededList[0] != '':
            replacementLists.append(embededList)
elif len(embededList) > 1:
    replacementLists.append(embededList)

for replacementList in replacementLists:
    x = 0
    while x < len(replacementList):
        webMap1 = replacementList[x].split(" ")[0]
        webMap2 = replacementList[x].split(" ")[1]
        expAppJSON = expAppJSON.replace(webMap1, webMap2)
        x += 1


# Replace portalUrl
compiled = re.compile(re.escape(sourcePortal), re.IGNORECASE)
expAppJSON = compiled.sub(targetPortal, expAppJSON)

# Check if exp app exists
exists = False
for result in target.content.search(f"title:{appTitle} AND owner:{targetOwner}", item_type='Web Experience'):
   if result['title'] == appTitle:
       expApp2 = result
       exists = True

# Get Exp App Properties
exp_app_properties = {'title': expApp.title,
                      'type': 'Web Experience',
                      'snippet': expApp.snippet,
                      'description': expApp.description,
                      'tags': expApp.tags,
                      'text': expAppJSON}

if exists == False:
    arcpy.AddMessage("Creating copy of Experience Builder App")
    if targetFolder == 'ROOT':
        expAppItem = target.content.add(item_properties=exp_app_properties, owner=targetOwner)
    else:
        expAppItem = target.content.add(item_properties=exp_app_properties, owner=targetOwner, folder=targetFolder)
elif exists == True:
    arcpy.AddMessage(f"Updating existing web app {expApp2.title}")
    expApp2.update(item_properties=exp_app_properties)
    expAppItem = expApp2

# Call Function to Download Experience Builder Application Resources
downloadExpAppResources(expApp)

# Append source/target portal info
replacementLists.append([sourcePortal + ' ' + targetPortal])
replacementLists.append([sourcePortal.rsplit('/', 1)[0] + ' ' + targetPortal.rsplit('/', 1)[0]])

# Add Resources to new Experience Builder App
arcpy.AddMessage("Adding Resources to new Experience Builder App")
for replacementList in replacementLists:
    for root, dirs, files in os.walk(scratchFolder, topdown=False):
        for name in files:
            if '.zip' not in name:
                if name == 'config.json':
                    # Update config JSON to reference new web map
                    for webMapID in replacementList:
                        # Read config.json file
                        with open(os.path.join(root, name), encoding="utf-8") as f:
                            data = json.load(f)
                        # Convert JSON to string
                        configJSON = json.dumps(data)
                        compiled = re.compile(re.escape(webMapID.split(" ")[0]), re.IGNORECASE)
                        updatedConfigJSON = compiled.sub(webMapID.split(" ")[1], configJSON)
                        # Convert string to python dictionary
                        data2 = json.loads(updatedConfigJSON)
                        with open(os.path.join(root, name), 'w', encoding="utf-8") as f:
                            json.dump(data2, f)

for root, dirs, files in os.walk(scratchFolder, topdown=False):
    for name in files:
        if '.zip' not in name:
            directory = root.split('Resources\\')[-1]
            if '\\' in directory:
                directory = directory.replace('\\', '/')
            # Add updated config.json back to application
            if exists == False:
                    expAppItem.resources.add(file=os.path.join(root, name), folder_name=directory, file_name=name)
            elif exists == True:
                    expAppItem.resources.update(file=os.path.join(root, name), folder_name=directory, file_name=name)

# Update Thumbnail
arcpy.AddMessage("Updating thumbnail")
updateThumbnail(expApp, expAppItem)

arcpy.AddMessage("Publishing Experience Builder App")
# status: Published will publish the application
app_properties = {'typeKeywords': 'status: Published'}
expAppItem.update(item_properties=app_properties)

# Call function to clear scratch workspace
clearScratchWorkspace()