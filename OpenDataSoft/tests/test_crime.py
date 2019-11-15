

fc = r'\\vgisdata\gis data\GeoDatabases\CrimeData.gdb\CrimeData'
with ap.da.SearchCursor(fc, '*') as cursor:
   for row in cursor:
      objid = row[0]
      crimeDataHash[objid] = row