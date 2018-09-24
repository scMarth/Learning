import arcpy, os

root_directory = r".."

relative_path_mxd_count = 0
absolute_path_mxd_count = 0
mxd_file_count = 0

def print_layer_info(mxd_path):
    print(mxd_path + ":")
    mxd = arcpy.mapping.MapDocument(mxd_path)

    for df in arcpy.mapping.ListDataFrames(mxd, "*"):
        lyr = arcpy.mapping.ListLayers(mxd, "", df)[0]
        if lyr.supports("dataSource"):
            print "\t" + lyr.name
            print "\t\t" + lyr.dataSource
    del mxd

def explore_folder(root_directory):
    global relative_path_mxd_count, absolute_path_mxd_count, mxd_file_count
    for filename in os.listdir(root_directory):
        fullpath = os.path.join(root_directory, filename)
        if not os.path.exists(fullpath):
            continue
        if os.path.isfile(fullpath):
            basename, extension = os.path.splitext(fullpath)
            if extension.lower() == ".mxd":
                print_layer_info(fullpath)
        else:
            explore_folder(fullpath)

explore_folder(root_directory)
