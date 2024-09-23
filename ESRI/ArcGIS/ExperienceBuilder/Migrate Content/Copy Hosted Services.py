import arcpy, shutil, os
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection

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

    # Export hosted feature service to FGD, and download to scratch folder
    arcpy.AddMessage("######################################################")
    arcpy.AddMessage(f"Processing {itemTitle}")
    export_name = itemTitle

    arcpy.AddMessage(f"Exporting {itemTitle}")
    result_item = item.export(export_name, 'File Geodatabase', wait=True)

    arcpy.AddMessage(f"Saving File Geodatabase to: {scratchFolder}")
    download_result = result_item.download(scratchFolder)

    arcpy.AddMessage(f"Deleted {itemTitle} File Geodatabase from source portal")
    result_item.delete()

    # Set Item Properties
    item_properties = {
        'title': itemTitle,
        'type': 'File Geodatabase',
        'description': item.description,
        'snippet': item.snippet,
        'tags': item.tags,
        'extent': item.extent,
        'accessInformation': item.accessInformation,
        'licenseInfo': item.licenseInfo
    }

    # Get thumbnail and metadata
    thumbnail_file = item.download_thumbnail(arcpy.env.scratchFolder)
    metadata_file = item.download_metadata(arcpy.env.scratchFolder)

    # Add File Geodatabase to portal
    arcpy.AddMessage(f"Adding {itemTitle} File Geodatabase to target portal")
    if targetFolder == 'ROOT':
        fgd = target.content.add(item_properties=item_properties, owner=targetOwner, data=download_result,
                                 thumbnail=thumbnail_file, metadata=metadata_file)
    else:
        fgd = target.content.add(item_properties=item_properties, owner=targetOwner, folder=targetFolder,
                                 data=download_result, thumbnail=thumbnail_file, metadata=metadata_file)

    # Publish File Geodatabase
    arcpy.AddMessage(f"Publishing {itemTitle} File Geodatabase")
    try:
        targetService = fgd.publish()
    except Exception as e:
        if 'already exists' in str(e):
            targetService = fgd.publish(overwrite=True)

    # Update Capabilities of service
    arcpy.AddMessage("Updating Serivce Capabilities")
    sourceFlyrCollection = FeatureLayerCollection.fromitem(item)
    targetFlyrCollection = FeatureLayerCollection.fromitem(targetService)
    existingDef = sourceFlyrCollection.properties
    existingDef.serviceItemId = targetService.id
    targetFlyrCollection.manager.update_definition(existingDef)

    # Update Thumbnail
    arcpy.AddMessage("Updating thumbnail")
    updateThumbnail(item, targetService)

    # Delete File Geodatabase from target portal and scratch folder
    arcpy.AddMessage(f"Deleting {itemTitle} File Geodatabase in target portal")
    fgd.delete()

# Call function to clear scratch workspace
clearScratchWorkspace()
