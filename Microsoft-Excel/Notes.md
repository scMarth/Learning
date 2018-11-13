In CSV files:

```
mxd,layer_name,data_source,broken
\\vgisdata\gis data\gis_projects\city maps\fire\station_areas\citywide\citywide 44 x 60 inch copy.mxd,250,000 to 1 million,d:\background\cities.sdc\cities,
```

when opened up in Excel, the second column will have text aligned to the right because the cell value '250' is displayed as a number.

To force Excel to read all values as a string: you can add `="(value)"`:

e.g.:

```
mxd,layer_name,data_source,broken
="\\vgisdata\gis data\gis_projects\city maps\fire\station_areas\citywide\citywide 44 x 60 inch copy.mxd",="250",000 to 1 million",="d:\background\cities.sdc\cities",=""
```
If you do this, however, entries like

`="250,000 to 1 million"`

will be split into two columns

The best way is to format it like the following:
```
mxd,layer_name,data_source,broken
"\\vgisdata\gis data\gis_projects\city maps\fire\station_areas\citywide\citywide 44 x 60 inch copy.mxd","250",000 to 1 million","d:\background\cities.sdc\cities",=""
```

This way, entries like
`="250,000 to 1 million"`

won't be split into two columns

You can then sort by opening the .csv in Excel and then clicking:

Sort & Filter -> Custom Sort -> Expand the selection -> check 'My data has headers'
