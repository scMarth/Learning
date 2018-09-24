import arcpy, os, datetime

root_directory = r".."

print(datetime.datetime.now())
print("")

arcpy.env.workspace = root_directory

featureclasses = arcpy.ListFeatureClasses()

for featureclass in featureclasses:
    print(featureclass)
    desc = arcpy.Describe(featureclass)
    print(desc)
    print("Feature Type:  " + desc.featureType)
    print("Shape Type :   " + desc.shapeType)
    print("Shape Field Name: " + desc.shapeFieldName)
    print("")
    # print featureclass.featureType

feature_datasets = arcpy.ListDatasets("*", "Feature")

for dataset in feature_datasets:
    featureclasses = arcpy.ListFeatureClasses

feature_classes = []
walk = arcpy.da.Walk(root_directory, datatype="Any", type="All")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        feature_classes.append(os.path.join(dirpath, filename))

for feature_class in feature_classes:
    print(feature_class)

print("")
print(datetime.datetime.now())

