import requests
import shutil

# url = "http://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/export?bbox=-3.443425669035958E7%2C-3140404.2101608403%2C3.443425669035958E7%2C1.9889226664351646E7&bboxSR=&layers=&layerDefs=&size=1920%2C1080&imageSR=&format=png&transparent=true&dpi=&time=&layerTimeOptions=&dynamicLayers=&gdbVersion=&mapScale=&f=html"
url = "http://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/export?bbox=-3.443425669035958E7%2C-3140404.2101608403%2C3.443425669035958E7%2C1.9889226664351646E7&bboxSR=&layers=&layerDefs=&size=1920%2C1080&imageSR=&format=png&transparent=true&dpi=&time=&layerTimeOptions=&dynamicLayers=&gdbVersion=&mapScale=&f=image"
path = "imageDL.png"
r = requests.get(url, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)