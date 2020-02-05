require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/Legend",
    "esri/PopupTemplate",
    "esri/layers/FeatureLayer",
    "esri/Graphic"
], function(Map, MapView, Legend, PopupTemplate, FeatureLayer, Graphic){
    var colors = getFirstNColors(12);
    var colorArrays = [];

    for (var i=0; i<colors.length; i++){
        colorArrays.push(hexToRgb(colors[i]));
    }

    var map = new Map({
        basemap: "gray"
    });

    var view = new MapView({
        container: "parked-over-3-days-per-district-map",
        map: map,
        center: [-121.6555013,36.6777372],
        zoom: 13
    });

    var featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
    });

    var numDistricts = 12;

    var colors = getFirstNColors(numDistricts);
    // convert to rgb for uniqueValueInfos below
    for (var i=0; i<colors.length; i++){
        colors[i] = hexToRgb(colors[i]);
    }

    var valueInfos = [];
    for (var i=0; i<colors.length; i++){
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
        })
    }

    // define renderer
    var renderer = {
        type: "unique-value",
        field: "typeName",
        field2: "district",
        fieldDelimiter: ", ",
        uniqueValueInfos: valueInfos
    }

    var popupTemplate = new PopupTemplate({
        title: "District: {district}"
    })

    featureLayer.renderer = renderer;
    featureLayer.popupTemplate = popupTemplate;

    // create a legend
    var legend = new Legend({
        view: view,
        layerInfos: [{
            layer: featureLayer,
            title: "Parked More Than 3 Days (Public Property) records per district"
        }]
    })

    // add the legend to the map
    view.ui.add(
        legend,
        "top-right"
    );

    // add the layer to the map
    map.add(featureLayer);
});