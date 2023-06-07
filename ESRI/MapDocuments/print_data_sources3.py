import arcpy, os, sys

# set up for environment
environment = os.environ["DATASTORE_ENVIRONMENT"]
gdb_number = os.environ["DATASTORE_GDB_NUMBER"]

if environment == "DEV":
    connection = r"D:\DatabaseConnection\DEV_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "TEST":
    connection = r"D:\DatabaseConnection\TEST_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "UAT":
    connection = r"D:\DatabaseConnection\UAT_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "STAGE" or environment == "STG" or environment == "STAGING":
    connection = r"D:\DatabaseConnection\STAGE_DATASTORE_{0}.sde\PROD_DATASTORE_01.AWS.".format(gdb_number)
elif environment == "PROD" or "Prod":
    connection = r"D:\DatabaseConnection\PROD_DATASTORE_01.sde\PROD_DATASTORE_01.AWS."

sde_path = connection.split(r'\PROD_DATASTORE_01')[0]
arcpy.env.workspace = sde_path

# List all feature classes, tables, and views
datasets = arcpy.ListDatasets(feature_type='ALL')
datasets += arcpy.ListTables()
datasets += arcpy.ListViews()

# Loop through each dataset and print information
for dataset in datasets:
    desc = arcpy.Describe(dataset)
    print("Name: {}".format(desc.name))
    print("Type: {}".format(desc.dataType))
    if desc.dataType in ["FeatureClass", "Table"] and hasattr(desc, "definitionQuery"):
        print("This is a Query Feature Class")