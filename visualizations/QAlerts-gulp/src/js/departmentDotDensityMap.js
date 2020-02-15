require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/Legend",
    "esri/PopupTemplate",
    "esri/layers/FeatureLayer",
    "esri/Graphic"
], function(Map, MapView, Legend, PopupTemplate, FeatureLayer, Graphic){
    let colors = getFirstNColors(13);
    let colorArrays = [];

    for (let i=0; i<colors.length; i++){
        colorArrays.push(hexToRgb(colors[i]));
    }

    // let colorStrings = generateSortedColorStrings(13);

    let map = new Map({
        basemap: "gray"
    });

    let view = new MapView({
        container: "department-dot-density-map",
        map: map,
        center: [-121.6555013,36.6777372],
        zoom: 13
    });

    let featureLayer = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
    });

    let departments = [
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
    let symbols = [];
    for (let i=0; i<departments.length; i++){

        let symbol = {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: [colorArrays[i].r, colorArrays[i].g, colorArrays[i].b, 1],
            // color: colorStrings[i],
            outline: {
                color: [0, 0, 0, 0]
            }
        };
        symbols.push(symbol);
    }

    // generate infos for uniqueValueInfos
    let infos = [];
    for (let i=0; i<departments.length; i++){
        infos.push({
            value: departments[i],
            symbol: symbols[i]
        });
    }

    // define renderer
    let renderer = {
        type: "unique-value",
        field: "dept",
        uniqueValueInfos: infos
    };

    // define popupTemplate
    let popupTemplate = new PopupTemplate({
        title: "Department: {dept}",
        content: QAlertsRequestDataPopupTemplateFieldContent
    });

    featureLayer.renderer = renderer;
    featureLayer.popupTemplate = popupTemplate;

    // add the layer to the map
    map.add(featureLayer);
    
    // create a legend
    let legend = new Legend({
        view: view,
        layerInfos: [{
            layer: featureLayer,
            title: "QAlerts Department Request Dot Density"
        }]
    });

    // add the legend to the map
    view.ui.add(
        legend,
        "top-right"
    );
});