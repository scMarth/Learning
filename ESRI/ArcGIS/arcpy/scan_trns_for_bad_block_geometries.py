# for troubleshooting issues with geometric calculations in MDR_trn_V

import arcpy, os, sys

#Set up for environment
environment = os.environ["PROJECT_ENVIRONMENT"]
gdb_number = os.environ["PROJECT_GDB_NUMBER"]

if environment == "DEV":
    connection = r"D:\DatabaseConnection\DEV_ENV_{0}.sde\PROD_ENV_01.AWS.".format(gdb_number)
elif environment == "TEST":
    connection = r"D:\DatabaseConnection\TEST_ENV_{0}.sde\PROD_ENV_01.AWS.".format(gdb_number)
elif environment == "UAT":
    connection = r"D:\DatabaseConnection\UAT_ENV_{0}.sde\PROD_ENV_01.AWS.".format(gdb_number)
elif environment == "STAGE" or environment == "STG" or environment == "STAGING":
    connection = r"D:\DatabaseConnection\STAGE_ENV_{0}.sde\PROD_ENV_01.AWS.".format(gdb_number)
elif environment == "PROD" or "Prod":
    connection = r"D:\DatabaseConnection\PROD_ENV_01.sde\PROD_ENV_01.AWS."

sde_path = connection.split('\\PROD_ENV_01.AWS')[0]
print('.sde connection: {}\n'.format(sde_path))

trns_to_analyze = [
    11575
]

blocks_evw = connection + "BLOCKS_EVW"

for trn in trns_to_analyze:

    print('analyzing trn number: {}'.format(trn))

    where = 'TRN = {} and IS_ACTIVE = 1'.format(trn)

    # query the blocks within that trn number
    block_oids = []
    with arcpy.da.SearchCursor(blocks_evw, ['OBJECTID'], where_clause=where) as sc:
        for row in sc:
            block_oids.append(row[0])

    print('\n\tblock_oids: {}\n'.format(block_oids))

    # convert to strings
    oids = [str(x) for x in block_oids]

    bad_block_geometry_found = None

    for i in range(len(oids)):
        selection = oids[0:i] + oids[i+1:]

        search_query = 'select geometry::STGeomFromWKB(geography::UnionAggregate(a.SHAPE).STAsBinary(), 4326).STCentroid().STX from PROD_ENV_01.aws.BLOCKS_EVW a where a.IS_ACTIVE=1 and a.OBJECTID in ({})'.format(','.join(selection))

        print('\tsearch query: {}\n'.format(search_query))

        print('\tOBJECTID not in query: {}\n'.format(oids[i]))
        
        sde_connection = arcpy.ArcSDESQLExecute(sde_path)

        try:
            result = sde_connection.execute(search_query) # execute select statement
            # print('\tbad geometry for block with OBJECTID = {}'.format(oids[i]))
            bad_block_geometry_found = oids[i]
        except Exception as e:
            pass

        # Clean up
        del sde_connection
    
    if bad_block_geometry_found:
        print('\ttrn number {}: bad block geometry found, block OBJECTID = {}'.format(trn, bad_block_geometry_found))