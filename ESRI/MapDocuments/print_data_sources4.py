import arcpy, os, sys

mxd_path = r'C:\Users\vincent.lantaca\Documents\Github\DATASTORE\src\mxd\DEV\SUPPORT_TEST.mxd'

mxd = arcpy.mapping.MapDocument(mxd_path)

print('mxd.relativePaths: ', mxd.relativePaths)

for lyr in arcpy.mapping.ListLayers(mxd):
    # print info from layer object
    print("credits: {}".format(lyr.credits))
    print("isBasemapLayer: {}".format(lyr.isBasemapLayer))
    print("isBroken: {}".format(lyr.isBroken))
    print("isFeatureLayer: {}".format(lyr.isFeatureLayer))
    print("isGroupLayer: {}".format(lyr.isGroupLayer))
    print("isNetworkAnalystLayer: {}".format(lyr.isNetworkAnalystLayer))
    print("isNetworkDatasetLayer: {}".format(lyr.isNetworkDatasetLayer))
    print("isRasterizingLayer: {}".format(lyr.isRasterizingLayer))
    print("isRasterLayer: {}".format(lyr.isRasterLayer))
    print("isServiceLayer: {}".format(lyr.isServiceLayer))
    print("maxScale: {}".format(lyr.maxScale))
    print("minScale: {}".format(lyr.minScale))

    if lyr.supports("BRIGHTNESS"):
        print("brightness: {}".format(lyr.brightness))
    if lyr.supports("CONTRAST"):
        print("contrast: {}".format(lyr.contrast))
    if lyr.supports("DATASETNAME"):
        print("datasetName: {}".format(lyr.datasetName))
    if lyr.supports("DATASOURCE"):
        print("dataSource: {}".format(lyr.dataSource))
    if lyr.supports("DEFINITIONQUERY"):
        print("definitionQuery: {}".format(lyr.definitionQuery))
    if lyr.supports("DESCRIPTION"):
        print("description: {}".format(lyr.description))
    if lyr.supports("LABELCLASSES"):
        print("labelClasses: {}".format(lyr.labelClasses))

        for lblClass in lyr.labelClasses:

            print('\tlabelClass className: {}'.format(lblClass.className))
            print('\tlabelClass expression: {}'.format(lblClass.expression))
            print('\tlabelClass SQLQuery: {}'.format(lblClass.SQLQuery))
            print('\tlabelClass showClassLabels: {}'.format(lblClass.showClassLabels))
            print('')
    if lyr.supports("LONGNAME"):
        print("longName: {}".format(lyr.longName))
    if lyr.supports("NAME"):
        print("name: {}".format(lyr.name))
    if lyr.supports("SERVICEPROPERTIES"):
        print("serviceProperties: {}".format(lyr.serviceProperties))
    if lyr.supports("SHOWLABELS"):
        print("showLabels: {}".format(lyr.showLabels))
    if lyr.supports("SYMBOLOGY"):
        print("symbology: {}".format(lyr.symbology))
    if lyr.supports("SYMBOLOGYTYPE"):
        print("symbologyType: {}".format(lyr.symbologyType))
    if lyr.supports("TIME"):
        print("time: {}".format(lyr.time))
    if lyr.supports("TRANSPARENCY"):
        print("transparency: {}".format(lyr.transparency))
    if lyr.supports("VISIBLE"):
        print("visible: {}".format(lyr.visible))
    if lyr.supports("WORKSPACEPATH"):
        print("workspacePath: {}".format(lyr.workspacePath))

        wp_desc = arcpy.Describe(lyr.workspacePath)
        print('workspace desc: {}'.format(wp_desc))
        print(wp_desc.workspaceType)

    desc = arcpy.Describe(lyr)
    print(desc.dataType)
    print(desc.datasetType)

    print('')