require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/Legend",
    "esri/PopupTemplate",
    "esri/layers/FeatureLayer",
    "esri/Graphic"
], function(Map, MapView, Legend, PopupTemplate, FeatureLayer, Graphic){
    var colors = getFirstNColors(13);
    var colorArrays = [];

    for (var i=0; i<colors.length; i++){
        colorArrays.push(hexToRgb(colors[i]));
    }

    // var colorStrings = generateSortedColorStrings(13);

    var map = new Map({
        basemap: "gray"
    });

    var view = new MapView({
        container: "department-dot-density-map",
        map: map,
        center: [-121.6555013,36.6777372],
        zoom: 13
    });

    var featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
    });

    var departments = [
        "CD-COMPLIANCE",
        "CDD-GENERAL",
        "FIR-ADMIN",
        "FIR-PREVENTION",
        "POL-ANIMAL SVCS",
        "POL-SPEC OPS",
        "POL-TRAFFIC",
        "PWK-AIRPT",
        "PWK-FACILITIES",
        "PWK-MAINT SVCS",
        "PWK-PARKING",
        "PWK-TRAFFIC & TRANSP",
        "PWK-WASTEWATER"
    ];

    departments = departments.sort(); // sort the departments

    // generate symbols
    var symbols = [];
    for (var i=0; i<departments.length; i++){

        var symbol = {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: [colorArrays[i].r, colorArrays[i].g, colorArrays[i].b, 1],
            // color: colorStrings[i],
            outline: {
                color: [0, 0, 0, 0]
            }
        }
        symbols.push(symbol);
    }

    // generate infos for uniqueValueInfos
    var infos = [];
    for (var i=0; i<departments.length; i++){
        infos.push({
            value: departments[i],
            symbol: symbols[i]
        })
    }

    // define renderer
    var renderer = {
        type: "unique-value",
        field: "dept",
        uniqueValueInfos: infos
    }

    // define popupTemplate
    var popupTemplate = new PopupTemplate({
        title: "Department: {dept}"
    })

    featureLayer.renderer = renderer;
    featureLayer.popupTemplate = popupTemplate;

    console.log(featureLayer);

    // add the layer to the map
    map.add(featureLayer);
    
    // create a legend
    var legend = new Legend({
        view: view,
        layerInfos: [{
            layer: featureLayer,
            title: "QAlerts Department Request Dot Density"
        }]
    })

    // add the legend to the map
    view.ui.add(
        legend,
        "top-right"
    );
});