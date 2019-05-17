import arcpy, numpy

old_fgdb = r'C:\path\stuff.gdb\thing1'
new_fgdb = r'C:\path\more_stuff.gdb\thing2'

old_fields = set()

fields1 = arcpy.ListFields(old_fgdb)
fields2 = arcpy.ListFields(new_fgdb)

for i in range(0, len(fields1)):
    old_fields.add(fields1[i].name)
    print("{}. {}".format(i, fields1[i].name))

print("")

for i in range(0, len(fields2)):
    if fields2[i].name in old_fields:
        print("{}. {}".format(i, fields2[i].name))
    else:
        print("{}. {} <============= (new)".format(i, fields2[i].name))