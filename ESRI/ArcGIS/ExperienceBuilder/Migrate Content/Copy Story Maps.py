import arcpy, json, os, zipfile, shutil, re, time
from arcgis.gis import GIS
from arcgis.apps.storymap.story import StoryMap


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


def downloadstoryMapResources(app):
    '''Function to download Story Map application resources'''

    # Download Story Map App Resources to scratch directory
    arcpy.AddMessage(f"Downloading Resources for {app.title}")
    app.resources.export(scratchFolder, 'Resources.zip')

    # Extract Zipped Resources
    arcpy.AddMessage(f"Extracting Resources for {app.title}")
    with zipfile.ZipFile(os.path.join(scratchFolder, 'Resources.zip'), 'r') as zip_ref:
        zip_ref.extractall(scratchFolder)


def removeDraftJSON(app):
    '''Function to download Story Map application resources'''

    # Download Story Map App Resources to scratch directory
    arcpy.AddMessage(f"Removing Draft JSON for {app.title}")
    for file in app.resources.list():
        if 'draft_' in file['resource']:
            app.resources.remove(file['resource'])


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

# Create scratch Directory
scratchFolder = os.path.join(arcpy.env.scratchFolder, 'Resources')
if not os.path.exists(scratchFolder):
    os.mkdir(scratchFolder)

# Get Story Map ID
arcpy.AddMessage("Getting Story Map ID")
storyMapID = content.split(' - ')[-1]
appTitle = source.content.get(storyMapID).title

# Get Story Map JSON
arcpy.AddMessage("Getting Story Map JSON")
storyMap = source.content.get(storyMapID)
storyMapDict = storyMap.get_data(try_json=True)

# Convert dict to JSON
arcpy.AddMessage("Converting dict to JSON")
storyMapJSON = json.dumps(storyMapDict)

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
        storyMapJSON = storyMapJSON.replace(webMap1, webMap2)
        x += 1


# Replace portalUrl
sourcePortalMachine = 'https://jake3.esri.com'
targetPortalMachine = 'https://ps0022245.esri.com'
compiled = re.compile(re.escape(sourcePortalMachine), re.IGNORECASE)
storyMapJSON = compiled.sub(targetPortalMachine, storyMapJSON)

# Check if Story Map exists
exists = False
for result in target.content.search(f"title:{appTitle} AND owner:{targetOwner}", item_type='StoryMap'):
   if result['title'] == appTitle:
       storyMap2 = result
       exists = True

# Get Story Map Properties
story_map_properties = {'title': storyMap.title,
                      'type': 'StoryMap',
                      'snippet': storyMap.snippet,
                      'description': storyMap.description,
                      'tags': storyMap.tags,
                      'text': storyMapJSON}

if exists == False:
    arcpy.AddMessage("Creating copy of Story Map App")
    if targetFolder == 'ROOT':
        storyMapItem = target.content.add(item_properties=story_map_properties, owner=targetOwner)
    else:
        storyMapItem = target.content.add(item_properties=story_map_properties, owner=targetOwner, folder=targetFolder)
elif exists == True:
    arcpy.AddMessage(f"Updating existing web app {storyMap2.title}")
    storyMap2.update(item_properties=story_map_properties)
    storyMapItem = storyMap2

# Call Function to Download Story Map Application Resources
downloadstoryMapResources(storyMap)

# Append source/target portal info
replacementLists.append([sourcePortal + ' ' + targetPortal])
replacementLists.append([sourcePortal.rsplit('/', 1)[0] + ' ' + targetPortal.rsplit('/', 1)[0]])

# Add Resources to new Story Map App
arcpy.AddMessage("Adding Resources to new Story Map App")
draftFile = False
for replacementList in replacementLists:
    for root, dirs, files in os.walk(scratchFolder, topdown=False):
        for name in files:
            if '.zip' not in name:
                if name == 'published_data.json':
                    # Update config JSON to reference new web map
                    for webMapID in replacementList:
                        # Read JSON file
                        with open(os.path.join(root, name), encoding="utf-8") as f:
                            data = json.load(f)
                        # Convert JSON to string
                        configJSON = json.dumps(data)
                        # Replace original web map ID with new web map ID
                        compiled = re.compile(re.escape(webMapID.split(" ")[0]), re.IGNORECASE)
                        updatedConfigJSON = compiled.sub(webMapID.split(" ")[1], configJSON)
                        # Convert string to python dictionary
                        data2 = json.loads(updatedConfigJSON)
                        with open(os.path.join(root, name), 'w', encoding="utf-8") as f:
                            json.dump(data2, f)

# Remove draft_<epoch> if StoryMap exists
if exists == True:
    removeDraftJSON(storyMapItem)
    for root, dirs, files in os.walk(scratchFolder, topdown=False):
        for name in files:
            if 'draft_' in name:
                os.remove(os.path.join(root, name))

# Create copy of published_data.json and name it draft_{epoch}
for root, dirs, files in os.walk(scratchFolder, topdown=False):
    for name in files:
        if name == 'published_data.json':
            if draftFile == False:
                epoch = int(time.time() * 1000)
                shutil.copy(os.path.join(root, name), os.path.join(root, f"draft_{epoch}.json"))
                draftFile = True

# Add updated JSON back to application
for root, dirs, files in os.walk(scratchFolder, topdown=False):
    for name in files:
        if '.zip' not in name:
            if exists == False:
                storyMapItem.resources.add(file=os.path.join(root, name), file_name=name)
            elif exists == True:
                if 'draft_' not in name:
                    try:
                        storyMapItem.resources.update(file=os.path.join(root, name), file_name=name)
                    except Exception as e:
                        if 'Resource does not exist' in str(e):
                            storyMapItem.resources.add(file=os.path.join(root, name), file_name=name)
                elif 'draft_' in name:
                    storyMapItem.resources.add(file=os.path.join(root, name), file_name=name)

# Remove files that no longer exist
sourceStoryMapFiles = []
for root, dirs, files in os.walk(scratchFolder, topdown=False):
    for name in files:
        if '.zip' not in name and 'draft_' not in name:
            sourceStoryMapFiles.append(name)
for file in storyMapItem.resources.list():
    if 'draft_' not in file['resource']:
        if file['resource'] not in sourceStoryMapFiles:
            storyMapItem.resources.remove(file['resource'])


# Update Thumbnail
arcpy.AddMessage("Updating thumbnail")
updateThumbnail(storyMap, storyMapItem)

arcpy.AddMessage("Publishing Story Map")
# status: Published will publish the application
app_properties = {'typeKeywords': 'status: Published'}
storyMapItem.update(item_properties=app_properties)
storyMapApp = StoryMap(storyMapItem, target)
if '.arcgis.com' in sourcePortal:
    storyMapApp.save(publish=True)

# Call function to clear scratch workspace
clearScratchWorkspace()