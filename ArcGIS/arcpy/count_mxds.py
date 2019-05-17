import arcpy, os, datetime

# root_directory = r".."
root_directory = r"M:"

mxd_count = 0
absolute_mxd_count = 0
relative_mxd_count = 0

def explore_folder(root_directory):
    global mxd_count, absolute_mxd_count, relative_mxd_count
    for filename in os.listdir(root_directory):
        try:
            # fullpath = os.path.join(root_directory, filename)
            symbolic_path = os.path.join(root_directory, filename)
            fullpath = os.path.abspath(symbolic_path)
            if (not os.path.isdir(fullpath)) and (not os.path.isfile(fullpath)) and (not os.path.exists(fullpath)):
                continue # skip invalid paths or paths with wierd filenames

            if os.path.isfile(fullpath):
                if filename.lower().endswith(".mxd"):
                    mxd_count += 1
                    mxd = arcpy.mapping.MapDocument(fullpath)
                    if mxd.relativePaths:
                        relative_mxd_count += 1
                    else:
                        absolute_mxd_count += 1
                    del mxd
            elif os.path.isdir(fullpath):
                explore_folder(fullpath)
        except:
            continue

print(datetime.datetime.now())
print("")

explore_folder(root_directory)

print("Number of .mxd files found: " + str(mxd_count))
print("Number of .mxd files using relative paths: " + str(relative_mxd_count))
print("Number of .mxd files using absolute paths: " + str(absolute_mxd_count))

print("")
print(datetime.datetime.now())

