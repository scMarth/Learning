# Note: You must use ArcPy for ArcGIS Desktop (Python 2.7.10) since ArcPy for ArcGIS Pro doesn't have arcpy.mapping.MapDocument

import arcpy, os, datetime, ntpath

root_directory = r".."

access_denied_paths = []
mxds = {} # mapping from mxd filename to an array of paths to a mxd with that filename
data_sources = {} # mapping from resource names to an array of paths to resources with that name
resource_drive_letters = []
resource_unc_locations = []


def print_mxd_type(mxd_path):
    mxd = arcpy.mapping.MapDocument(mxd_path)
    if mxd.relativePaths:
        print("RELATIVE MXD:")
    else:
        print("ABSOLUTE MXD:")
    del mxd

def print_layer_info(lyr):
    if lyr.supports("dataSource"):
        print("dataSource: " + lyr.dataSource)
    if lyr.supports("datasetName"):
        print("datasetName: " + lyr.datasetName)
    if lyr.supports("longName"):
        print("longName: " + lyr.longName)
    if lyr.supports("name"):
        print("name: " + lyr.name)
    if lyr.supports("workspacePath"):
        print("workspacePath: " + lyr.workspacePath)
        splitunc = os.path.splitunc(lyr.workspacePath)
        if not (splitunc[0] == ""):
            print(splitunc[0])
            print(splitunc[1])
            test_path = os.path.join("M:\\", splitunc[1])
            print(test_path)
    print("")


def add_path_to_mxds(mxds, filename, fullpath):
    if filename in mxds:
        if fullpath in mxds[filename]:
            return
        else:
            mxds[filename].append(fullpath)
    else:
        mxds[filename] = [fullpath]

def store_data_sources(data_sources, mxd_path):
    mxd = arcpy.mapping.MapDocument(mxd_path)

    for lyr in arcpy.mapping.ListLayers(mxd):
        if lyr.supports("dataSource") and lyr.supports("workspacePath"):

            # print_layer_info(lyr)
            data_path = lyr.dataSource
            # splunc = os.path.abspath(data_path)
            # print(splunc)
            # print("unc: " + splunc)
            # print("rest: " + rest)

            if lyr.name in data_sources:
                if data_path in data_sources[lyr.name]:
                    return
                else:
                    data_sources[lyr.name].append(data_path)
            else:
                data_sources[lyr.name] = [data_path]
    del mxd

def explore_folder(root_directory, mxds, data_sources, access_denied_paths):
    for filename in os.listdir(root_directory):
        try:
            symbolic_path = os.path.join(root_directory, filename)
            fullpath = os.path.abspath(symbolic_path)
            # fullpath = os.path.join(root_directory, filename)
            if (not os.path.isdir(fullpath)) and (not os.path.isfile(fullpath)) and (not os.path.exists(fullpath)):
                continue # skip invalid paths or paths with wierd filenames

            if os.path.isfile(fullpath):
                if filename.lower().endswith(".mxd"):
                    # print_mxd_type(fullpath)
                    add_path_to_mxds(mxds, filename, fullpath)
                    store_data_sources(data_sources, fullpath)
                    # print("")
                    # print("")
                    # print("")
            elif os.path.isdir(fullpath):
                explore_folder(fullpath, mxds, data_sources, access_denied_paths)
        except:
            access_denied_paths.append(os.path.join(root_directory, filename))
            continue

def dump_str_to_arr_hash(hashmap):
    for key in hashmap:
        print(key)
        array = hashmap[key]

        for string in array:
            print("\t" + string)

print(datetime.datetime.now())
print("")

print("Exploring path: '" + root_directory + "'")
explore_folder(root_directory, mxds, data_sources, access_denied_paths)
print("")

# print("Dumping .mxds:")
# dump_str_to_arr_hash(mxds)
# print("")
# print("Dumping data sources:")
# dump_str_to_arr_hash(data_sources)
# print("")


print("")
print(datetime.datetime.now())




