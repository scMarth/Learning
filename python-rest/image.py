import requests

r = requests.get('http://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/export?bbox=-3.443425669035958E7%2C-3140404.2101608403%2C3.443425669035958E7%2C1.9889226664351646E7&bboxSR=&layers=&layerDefs=&size=1920%2C1080&imageSR=&format=png&transparent=true&dpi=&time=&layerTimeOptions=&dynamicLayers=&gdbVersion=&mapScale=&f=html')
r.raw
