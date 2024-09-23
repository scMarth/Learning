import arcpy, tempfile, shutil, os
from arcgis.gis import GIS

# Variables
sourcePortal = arcpy.GetParameterAsText(0)
sourceIWA = arcpy.GetParameterAsText(1)
sourceUsername = arcpy.GetParameterAsText(2)
sourcePassword = arcpy.GetParameterAsText(3)
sourceUser = arcpy.GetParameterAsText(4)
content = arcpy.GetParameterAsText(5)
targetPortal = arcpy.GetParameterAsText(6)
targetIWA = arcpy.GetParameterAsText(7)
targetUsername = arcpy.GetParameterAsText(8)
targetPassword = arcpy.GetParameterAsText(9)
targetOwner = arcpy.GetParameterAsText(10)
targetFolder = arcpy.GetParameterAsText(11)
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

# Item Keywords
FILE_BASED_ITEM_TYPES = frozenset(['File Geodatabase','CSV', 'Image', 'KML', 'Locator Package',
                                  'Map Document', 'Shapefile', 'Microsoft Word', 'PDF', 'Form',
                                  'Microsoft Powerpoint', 'Microsoft Excel', 'Layer Package',
                                  'Mobile Map Package', 'Geoprocessing Package', 'Service Definition',
                                  'Scene Package', 'Tile Package', 'Vector Tile Package'])

ITEM_COPY_PROPERTIES = ['title', 'type', 'typeKeywords', 'description', 'tags',
                        'snippet', 'extent', 'spatialReference', 'name',
                        'accessInformation', 'licenseInfo', 'culture', 'url']

# Sign into source portal
arcpy.AddMessage("Signing into source portal")
source = GIS(sourcePortal, sourceUsername, sourcePassword, verify_cert=False)

# Sign into target portal
arcpy.AddMessage("Signing into target portal")
target = GIS(targetPortal, targetUsername, targetPassword, verify_cert=False)

# Get Hosted Feature Service ID
for val in content.split(';'):
    itemID = val.split(' - ')[-1]
    itemID = itemID.replace("'", "")
    itemID = itemID.replace('"', "")
    itemTitle = source.content.get(itemID).title
    item = source.content.get(itemID)

    # Check if item exists in Target Portal
    arcpy.AddMessage("######################################################")
    searchResult = target.content.search("title:" + item.title + " AND owner:" + targetOwner, item_type = item.type)
    if len(searchResult) > 0:
        targetItem = searchResult[0]
        arcpy.AddMessage(f"{itemTitle} found in target portal-----Deleting")
        targetItem.delete()

    # Add Item to Portal
    arcpy.AddMessage(f"Adding {itemTitle} to target portal")
    item_properties = {}
    for property_name in ITEM_COPY_PROPERTIES:
        item_properties[property_name] = item[property_name]

    data_file = item.download(arcpy.env.scratchFolder)

    thumbnail_file = item.download_thumbnail(arcpy.env.scratchFolder)
    metadata_file = item.download_metadata(arcpy.env.scratchFolder)

    # Add the item to the target portal, assign owner and folder
    if targetFolder == 'ROOT':
        target_item = target.content.add(item_properties, data_file, thumbnail_file,
                                     metadata_file, owner=targetOwner)
    else:
        target_item = target.content.add(item_properties, data_file, thumbnail_file,
                                         metadata_file, owner=targetOwner, folder=targetFolder)

# Call function to clear scratch workspace
clearScratchWorkspace()