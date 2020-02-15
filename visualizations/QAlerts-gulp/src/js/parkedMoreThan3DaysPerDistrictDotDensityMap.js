require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/Legend",
    "esri/PopupTemplate",
    "esri/layers/FeatureLayer",
    "esri/Graphic"
], function(Map, MapView, Legend, PopupTemplate, FeatureLayer, Graphic){
    let numDistricts = 12;
    let colors = getFirstNColors(numDistricts);
    let colorArrays = [];

    for (let i=0; i<colors.length; i++){
        colorArrays.push(hexToRgb(colors[i]));
    }

    let map = new Map({
        basemap: "gray"
    });

    let view = new MapView({
        container: "parked-over-3-days-per-district-map",
        map: map,
        center: [-121.6555013,36.6777372],
        zoom: 13
    });

    let featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
    });

    // convert to rgb for uniqueValueInfos below
    for (let i=0; i<colors.length; i++){
        colors[i] = hexToRgb(colors[i]);
    }

    let valueInfos = [];
    for (let i=0; i<colors.length; i++){
        valueInfos.push({
            value: "Parked More Than 3 Days (Public Property)" + ", " + (i+1).toString(),
            symbol: {
                type: "simple-marker",
                style: "circle",
                size: 3,
                outline: {
                    color: [0, 0, 0, 0]
                },
                color: [colors[i].r, colors[i].g, colors[i].b, 1]
            }
        });
    }

    // define renderer
    let renderer = {
        type: "unique-value",
        field: "typeName",
        field2: "district",
        fieldDelimiter: ", ",
        uniqueValueInfos: valueInfos
    };

    let popupTemplate = new PopupTemplate({
        title: "District: {district}",
        content: QAlertsRequestDataPopupTemplateFieldContent
    });

    featureLayer.renderer = renderer;
    featureLayer.popupTemplate = popupTemplate;

    // create a legend
    let legend = new Legend({
        view: view,
        layerInfos: [{
            layer: featureLayer,
            title: "Parked More Than 3 Days (Public Property) records per district"
        }]
    });

    // add the legend to the map
    view.ui.add(
        legend,
        "top-right"
    );

    // add the layer to the map
    map.add(featureLayer);
});