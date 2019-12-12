require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/Legend",
    "esri/PopupTemplate",
    "esri/layers/FeatureLayer",
    "esri/Graphic"
], function(Map, MapView, Legend, PopupTemplate, FeatureLayer, Graphic){

    var map = new Map({
        basemap: "gray"
    });

    var view = new MapView({
        container: "gang-related-crime-map",
        map: map,
        center: [-121.6555013,36.6777372],
        zoom: 13
    });

    var featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Anonymized_Crime_Data/MapServer/0"
    });

    featureLayer.when(() => {
        // define symbol for non-gang-related crimes
        var nonGangRelatedSymbol = {
            type: "simple-marker",
            size: 3,
            color: [0, 0, 0, 1],
            outline: {
                color: [0, 0, 0, 0]
            }        
        }

        // define symbol for gang related crimes
        var gangRelatedSymbol = {
            type: "simple-marker",
            size: 6,
            color: [255, 0, 0, 1],
            outline: {
                color: [0, 0, 0, 0]
            }
        }

        // create the renderer
        var renderer = {
            type: "unique-value",
            field: "GangRpt",
            defaultSymbol: nonGangRelatedSymbol,
            uniqueValueInfos: [
                {
                    value: 'Y',
                    symbol: gangRelatedSymbol,
                    label: 'Gang Related'
                }
            ]
        }

        // construct fieldInfos for popup template
        var fieldInfos = [];

        featureLayer.fields.forEach(item => {
            fieldInfos.push({
                fieldName: item.name,
                label: item.alias,
                visible: true
            });
        });

        // create popup template
        var popupTemplate = {
            title: "Record {OBJECTID}",
            content: [{
                type: "fields",
                fieldInfos: fieldInfos
            }]
        }

        // set layer and popup template
        featureLayer.renderer = renderer;
        featureLayer.popupTemplate = popupTemplate;

        // create a legend
        var legend = new Legend({
            view: view,
            layerInfos: [{
                layer: featureLayer,
                title: "Gang Related Crime Map"
            }]
        });

        // add the legend to the map
        view.ui.add(
            legend,
            "top-right"
        );
    });



    // add the layer to the map
    map.add(featureLayer);
});