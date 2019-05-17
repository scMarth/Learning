import arcpy, os, sys

root_directory = r".."

access_denied_paths = []
mxds = {} # mapping from mxd filename to an array of paths to a mxd with that filename
data_sources = {} # mapping from resource names to an array of paths to resources with that name

def store_mxd_data(mxd_path):
    global data_sources
    print (mxd_path)

    if mxd_path in data_sources:
        sys.stderr.write('Error: Same .mxd file processed twice.')
        sys.exit()
    else:
        data_sources[mxd_path] = []
        mxd = arcpy.mapping.MapDocument(mxd_path)

        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.supports("DATASOURCE"):
                print "\t" + lyr.name
                print "\t\t" + lyr.dataSource
        del mxd

def explore_folder(root_directory):
    global data_soures
    for filename in os.listdir(root_directory):
        fullpath = os.path.join(root_directory, filename)
        if not os.path.exists(fullpath):
            continue
        if os.path.isfile(fullpath):
            basename, extension = os.path.splitext(fullpath)
            if extension.lower() == ".mxd":
                store_mxd_data(fullpath)
        else:
            explore_folder(fullpath)

explore_folder(root_directory)
