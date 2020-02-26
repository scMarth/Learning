import arcpy, os, datetime

root_directory = r".."
# root_directory = r"M:"

weird_paths_count = 0
weird_paths = []
access_denied_paths = []

def explore_folder(root_directory):
    global weird_paths, weird_paths_count, access_denied_paths
    for filename in os.listdir(root_directory):
        try:
            fullpath = os.path.join(root_directory, filename)

            if os.path.isfile(fullpath):
                continue
            elif os.path.isdir(fullpath):
                explore_folder(fullpath)
            elif (not os.path.isdir(fullpath)) and (not os.path.isfile(fullpath)) and (not os.path.exists(fullpath)):
                weird_paths_count += 1
                weird_paths.append(fullpath)
        except:
            access_denied_paths.append(os.path.join(root_directory, filename))
            continue

def print_string_array(string_array):
    for string in string_array:
        print(string)

print(datetime.datetime.now())
print("")
    
explore_folder(root_directory)

print("Exploring path: '" + root_directory + "'")
print("Weird paths found: " + str(weird_paths_count))

print("")
print_string_array(weird_paths)

print("")
print_string_array(access_denied_paths)

print("")
print(datetime.datetime.now())
