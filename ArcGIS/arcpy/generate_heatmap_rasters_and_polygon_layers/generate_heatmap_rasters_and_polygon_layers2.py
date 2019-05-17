'''

Generates a Kernel Density Raster Heatmap for the list of projects, and creates a second verson that is clipped to
city boundaries. The result is stored wherever the defined workspace is.

Call in PowerShell with:
& 'C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe' 'C:\path\script.py'

Takes long (hours) to run with cell size = 10

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
def generate_binned_shapefiles(projectPath, inputRaster, num_bins_list):
    intRas = Int(Raster(inputRaster))

    intPolygon = projectPath + r'\int_simplified.shp'
    arcpy.RasterToPolygon_conversion(intRas, intPolygon, 'SIMPLIFY', 'VALUE') # do the conversion

    rasterMax = arcpy.GetRasterProperties_management(intRas, 'MAXIMUM')
    rasterMax = float(rasterMax.getOutput(0))

    for num_bins in num_bins_list:
        remapRange = RemapRange(get_remap_table_for_remap_range(num_bins, rasterMax))
        binnedRas = Reclassify(intRas, 'VALUE', remapRange,'NODATA')
        # location of temporary polygon
        tempPolygon = projectPath + '\\' + str(num_bins) + '_bins_simplified.shp'
        arcpy.RasterToPolygon_conversion(binnedRas, tempPolygon, 'SIMPLIFY', 'VALUE') # do the conversion
        tempPolygon2 = projectPath + '\\' + str(num_bins) + '_bins_notsimplified.shp'
        arcpy.RasterToPolygon_conversion(binnedRas, tempPolygon2, 'NO_SIMPLIFY', 'VALUE') # do the conversion

def clear_directory(directory_path):
    for file in os.listdir(directory_path):
        filePath = os.path.join(directory_path, file)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
        except:
            pass

def generate_heatmap_rasters_and_polygons(projectPath, extent, cellSize, projectName, inputFc, cityBoundary, bins):
    rasterPath = projectPath + '\\' + projectName + '.tif'
    rasterClipped = projectPath + '\\' + projectName + 'Clipped.tif'
    populationField = 'NONE'

    # clear the project path
    clear_directory(projectPath)

    # execute KernelDensity
    if cellSize is not None:
        outKernelDensity = KernelDensity(inputFc, populationField, cellSize)
    else:
        outKernelDensity = KernelDensity(inputFc, populationField)

    # save the output
    outKernelDensity.save(rasterPath)

    # save the clipped raster
    arcpy.Clip_management(rasterPath, extent, rasterClipped, \
        in_template_dataset=cityBoundary, clipping_geometry='ClippingGeometry', \
        maintain_clipping_extent='NO_MAINTAIN_EXTENT')

    generate_binned_shapefiles(projectPath, rasterClipped, bins)

workspace = r'C:\user\test\heatmap-dev'
extent = '5773500 2124000 5807250 2161800'
cityBoundary = r'C:\user\test\CityBoundary.gdb\SalinasBoundary'
cellSize = None # same cell size as burglary raster

env.workspace = workspace # set workspace
arcpy.env.extent = extent # set extent
arcpy.CheckOutExtension('Spatial') # check out the ArcGIS Spatial Analyst extension license

projects = [
    # {
    #     'projectName' : 'anonCrimeHeatmap',
    #     'featureClass' : r'C:\user\test\anonCrimeData.gdb\anonCrimeData',
    #     'bins' : [10, 50, 100, 150]
    # },
    {
        'projectName' : 'collisionsHeatmap',
        'featureClass' : r'C:\user\test\Traffic.gdb\Collision_Data',
        'bins' : [10, 50, 100, 150]
    }
]

for project in projects:
    projectPath = workspace + '\\' + project['projectName']
    if not os.path.isdir(projectPath):
        os.mkdir(projectPath)
    generate_heatmap_rasters_and_polygons(projectPath, extent, cellSize, project['projectName'], project['featureClass'], cityBoundary, project['bins'])