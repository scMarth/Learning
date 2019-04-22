'''

Generates a Kernel Density Raster Heatmap for the anonymized crime data, and creates a second verson that is clipped to
city boundaries. The result is in: C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap

Call in PowerShell with:
& 'C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe' 'C:\path\script.py'

'''

import arcpy, os, shutil, sys
from arcpy import env
from arcpy.sa import *

def get_remap_table_for_remap_range(num_bins, MAXIMUM):
    result = []
    MAXIMUM = float(MAXIMUM)
    for i in range(num_bins):
        lower_range = i * (MAXIMUM/num_bins)
        upper_range = (i + 1) * (MAXIMUM/num_bins)
        result.append([lower_range, upper_range, i+1])
    return result

# generate shapefiles with raster values put into bins
def generate_binned_shapefiles(inputRaster, num_bins_list):
    intRas = Int(Raster(inputRaster))
    intPolygon = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\int_simplified.shp'
    intPolygon2 = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\int_notsimplified.shp'
    arcpy.RasterToPolygon_conversion(intRas, intPolygon, 'SIMPLIFY', 'VALUE') # do the conversion
    arcpy.RasterToPolygon_conversion(intRas, intPolygon2, 'NO_SIMPLIFY', 'VALUE') # do the conversion
    rasterMax = arcpy.GetRasterProperties_management(intRas, 'MAXIMUM')
    rasterMax = float(rasterMax.getOutput(0))

    for num_bins in num_bins_list:
        remapRange = RemapRange(get_remap_table_for_remap_range(num_bins, rasterMax))
        binnedRas = Reclassify(intRas, 'VALUE', remapRange,'NODATA')
        # location of temporary polygon
        tempPolygon = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\\' + str(num_bins) + '_bins_simplified.shp'
        arcpy.RasterToPolygon_conversion(binnedRas, tempPolygon, 'SIMPLIFY', 'VALUE') # do the conversion
        tempPolygon2 = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\\' + str(num_bins) + '_bins_notsimplified.shp'
        arcpy.RasterToPolygon_conversion(binnedRas, tempPolygon2, 'NO_SIMPLIFY', 'VALUE') # do the conversion

# set workspace
workspace = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap'
env.workspace = workspace

# set output extent
extent = '5773500 2124000 5807250 2161800'
arcpy.env.extent = extent

# arcpy.env.rasterStatistics = 'NONE'
# arcpy.env.rasterStatistics = 'STATISTICS'

# check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension('Spatial')

# set local variables
anonCrimeDataFc = r'C:\user\test\anonCrimeData.gdb\anonCrimeData'
cityBoundary = r'M:\GeoDatabases\CityBoundary.gdb\SalinasBoundary'
anonCrimeRasterPath = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\anonCrimeData.tif'
anonCrimeRasterClipped = r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\anonCrimeDataClipped.tif'
populationField = 'NONE'
cellSize = 10

# clear output directory
for file in os.listdir(workspace):
    filePath = os.path.join(workspace, file)
    try:
        if os.path.isfile(filePath):
            os.unlink(filePath)
    except:
        pass

# execute KernelDensity
outKernelDensity = KernelDensity(anonCrimeDataFc, populationField, cellSize)

# save the output 
# outKernelDensity.save(r'C:\user\Documents\workspace\heatmap-dev\anonCrimeHeatmap\output.png') # png errors out and creates a tif
outKernelDensity.save(anonCrimeRasterPath) # tif works fine

# save the clipped raster
arcpy.Clip_management(anonCrimeRasterPath, extent, anonCrimeRasterClipped,
    in_template_dataset=cityBoundary, clipping_geometry='ClippingGeometry',
    maintain_clipping_extent='MAINTAIN_EXTENT')

generate_binned_shapefiles(anonCrimeRasterClipped, [10, 50, 100, 150])