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
        container: "origin-dot-density-map",
        map: map,
        center: [-121.6555013,36.6777372],
        zoom: 13
    });

    var featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
    });

    // a list of origins
    var origins = [
        'Call Center',
        'Control Panel',
        'QAlert Mobile iOS',
        'Report2Gov Android',
        'Report2Gov Website',
        'Report2Gov iOS',
        'Text Message',
        'Website'
    ];

    // map origins to origin types
    var originTypes = {
        'Call Center' : 'Call Center',
        'Control Panel' : 'Control Panel',
        'QAlert Mobile iOS' : 'Mobile',
        'Report2Gov Android' : 'Mobile',
        'Report2Gov Website' : 'Website',
        'Report2Gov iOS' : 'Mobile',
        'Text Message' : 'Mobile',
        'Website' : 'Website'
    };

    // map origin types to a unique symbol id
    var originTypeSymbolMap = {
        'Call Center' : 0,
        'Control Panel' : 1,
        'Mobile' : 2,
        'Website' : 3
    }

    // create 4 symbols since we have 4 origin types
    var symbols = [
        {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: "red",
            outline: {
                color: [0, 0, 0, 0]
            }
        },
        {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: [0, 176, 60, 1],
            outline: {
                color: [0, 0, 0, 0]
            }
        },
        {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: "blue",
            outline: {
                color: [0, 0, 0, 0]
            }
        },
        {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: [255, 255, 102],
            outline: {
                color: [0, 0, 0, 0]
            }
        }
    ]

    // generate infos for uniqueValueInfos
    var infos = [];
    for (var i=0; i<origins.length; i++){
        var symbolsInd = originTypeSymbolMap[originTypes[origins[i]]];

        infos.push({
            value: origins[i],
            symbol: symbols[symbolsInd]
        });
    }

    // define renderer
    var renderer = {
        type: "unique-value",
        field: "origin",
        uniqueValueInfos: infos
    }

    var popupTemplate = new PopupTemplate({
        title: "Origin: {origin}"
    })

    featureLayer.renderer = renderer;
    featureLayer.popupTemplate = popupTemplate;

    // create a legend
    var legend = new Legend({
        view: view,
        layerInfos: [{
            layer: featureLayer,
            title: "QAlerts Request Origin Type Dot Density"
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