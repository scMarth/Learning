import arcpy, os

# set up for environment
environment = os.environ["SCRAPWORK_ENVIRONMENT"]
gdb_number = os.environ["SCRAPWORK_GDB_NUMBER"]

if environment == "DEV":
    connection = r"D:\DatabaseConnection\DEV_SCRAPWORK_{0}.sde\CONN.AWS.".format(gdb_number)
elif environment == "TEST":
    connection = r"D:\DatabaseConnection\TEST_SCRAPWORK_{0}.sde\CONN.AWS.".format(gdb_number)
elif environment == "UAT":
    connection = r"D:\DatabaseConnection\UAT_SCRAPWORK_{0}.sde\CONN.AWS.".format(gdb_number)
elif environment == "STAGE" or environment == "STG" or environment == "STAGING":
    connection = r"D:\DatabaseConnection\STAGE_SCRAPWORK_{0}.sde\CONN.AWS.".format(gdb_number)
elif environment == "PROD" or "Prod":
    connection = r"D:\DatabaseConnection\CONN.sde\CONN.AWS."

sde_connection = connection.split('\\CONN.AWS')[0]

# Establish a connection to the geodatabase
arcpy.env.workspace = sde_connection

# Get a list of all feature classes and tables
data_list = arcpy.ListTables() + arcpy.ListFeatureClasses()

# Iterate through each feature class or table
for data in data_list:

    # if (data != 'CONN.AWS.APPLICATION_BLOCKS') and (data != 'CONN.AWS.RANCH_APPLICATION_BLOCKS'):
    #     continue

    # Get the list of relationships for the current data
    try:
        relationships = arcpy.Describe(data).relationshipClassNames
    except:
        continue


    
    # Check if the data has any relationships
    if relationships:
        print("Data: {}".format(data))
        print("Relationships:")
        for relationship in relationships:
            print("\t{}".format(relationship))
            describe_rel = arcpy.Describe(relationship)
            cardinality = describe_rel.cardinality
            print("\t\tdescribe_rel: {}".format(describe_rel))
            print("\t\tcardinality: {}".format(cardinality))
            print('\t\toriginClassKeys: {}'.format(describe_rel.originClassKeys))
            print('\t\toriginClassNames: {}'.format(describe_rel.originClassNames))
            print('\t\tdestinationClassKeys: {}'.format(describe_rel.destinationClassKeys))
            print('\t\tdestinationClassNames: {}'.format(describe_rel.destinationClassNames))
    else:
        continue
    
    print("\n")
