require([
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/FeatureLayer",
    "esri/layers/support/LabelClass",
    "esri/PopupTemplate",
    "esri/widgets/Legend"
], function(Map, MapView, FeatureLayer, LabelClass, PopupTemplate, Legend) {

    let map = new Map({
        basemap: "gray"
    });

    let view = new MapView({
        container: "district-map",
        map: map,

        center: [-121.6555013,36.69],
        zoom: 13
    });

    // convert hex to Rgb
    // https://stackoverflow.com/questions/5623838/rgb-to-hex-and-hex-to-rgb
    function hexToRgb(hex){
        let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }

    let numDistricts = 12;

    let colors = getFirstNColors(numDistricts);
    // convert to rgb for uniqueValueInfos below
    for (let i=0; i<colors.length; i++){
        colors[i] = hexToRgb(colors[i]);
    }

    let valueInfos = [];

    for (let i=0; i<colors.length; i++){
        valueInfos.push({
            value: (i+1).toString(),
            symbol: {
                type: "simple-fill",
                outline: {
                    color: [0, 0, 0, 0.5]
                },
                color: [colors[i].r, colors[i].g, colors[i].b, 0.75]
            },
            labels: (i+1).toString()
        });
    }

    /********************
    * Add feature layer
    ********************/
    let customRenderer = {
        type: "unique-value",
        "field": "BEAT_NO",
        "field2": null,
        "field3": null,
        uniqueValueInfos: valueInfos
    };

    let customLabels = new LabelClass({
        labelExpression: "[BEAT_NO]",
        symbol: {
            type: "text",
            color: [0, 0, 0, 1],
            haloColor: [0, 0, 0, 1],
            haloSize: 0
        }
    });

    // Carbon storage of trees in Warren Wilson College.
    let featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/PoliceBeats/MapServer/0",
        renderer: customRenderer,
        labelingInfo: customLabels,
        popupTemplate: new PopupTemplate({
            title: "District {BEAT_NO}"
        }),
        minScale: 0, // make sure the feature layer is visible for all extents
        maxScale: 0  // make sure the feature layer is visible for all extents
    });

    map.add(featureLayer);

    view.when(function(){
        // get the first layer in the collection of operational layers in the WebMap
        // when the resources in the MapView have loaded.
        let featureLayer = map.layers.getItemAt(0);
        let legend = new Legend({
            view: view,
            layerInfos: [
                {
                    layer: featureLayer,
                    title: "Police Beat Districts"
                }
            ]
        });
        // Add widget to the bottom right corner of the view
        view.ui.add(legend, "bottom-left");

    });
});