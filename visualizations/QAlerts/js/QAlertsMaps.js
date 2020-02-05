require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/Legend",
    "esri/PopupTemplate",
    "esri/layers/FeatureLayer",
    "esri/Graphic"
], function(Map, MapView, Legend, PopupTemplate, FeatureLayer, Graphic){


    var maps = {
        department: {
            containerId: "department-dot-density-map",
            numColors: 13,
            fields: [
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
            ]
        },
        origin: {
            containerId: "origin-dot-density-map",
            numColors: 12
        }
    }

    maps.department.fields.sort();

    var test = new FeatureLayer({
        url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
    });

    for (var key in maps){
        maps[key]['colors'] = getFirstNColors(maps[key].numColors);
        maps[key]['colorArrays'] = [];
        for (var i=0; i<maps[key].numColors; i++){
            maps[key]['colorArrays'].push(hexToRgb(maps[key].colors[i]));
        }

        maps[key]['map'] = new Map({
            basemap: "gray"
        });

        maps[key]['view'] = new MapView({
            container: maps[key].containerId,
            map: maps[key].map,
            center: [-121.6555013,36.6777372],
            zoom: 13
        });

        maps[key].featureLayer = new FeatureLayer({
            url: "https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/WebLayers/QScendRequestData/MapServer/0"
        });

        // maps[key].featureLayer = test;

    }

    /*******************************************************************
    * Department Data
    *******************************************************************/

    // generate symbols
    var departmentSymbols = [];
    for (var i=0; i<maps.department.fields.length; i++){
        var symbol = {
            type: "simple-marker",
            style: "circle",
            size: 3,
            color: [maps.department.colorArrays[i].r, maps.department.colorArrays[i].g, maps.department.colorArrays[i].b, 1],
            // color: colorStrings[i],
            outline: {
                color: [0, 0, 0, 0]
            }
        }
        departmentSymbols.push(symbol);
    }

    // generate infos for uniqueValueInfos
    var departmentInfos = [];
    for (var i=0; i<maps.department.fields.length; i++){
        departmentInfos.push({
            value: maps.department.fields[i],
            symbol: departmentSymbols[i]
        })
    }

    // define renderer
    var departmentRenderer = {
        type: "unique-value",
        field: "dept",
        uniqueValueInfos: departmentInfos
    }

    // define popupTemplate
    var departmentPopupTemplate = new PopupTemplate({
        title: "Department: {dept}"
    })

    maps.department.featureLayer.renderer = departmentRenderer;
    maps.department.featureLayer.popupTemplate = departmentPopupTemplate;

    maps.department.map.add(maps.department.featureLayer);

    /*******************************************************************
    * Origin Data
    *******************************************************************/

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

    var originSymbols = [
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
    var originInfos = [];
    for (var i=0; i<origins.length; i++){
        var symbolsInd = originTypeSymbolMap[originTypes[origins[i]]];

        originInfos.push({
            value: origins[i],
            symbol: originSymbols[symbolsInd]
        });
    }

    var originRenderer = {
        type: "unique-value",
        field: "origin",
        uniqueValueInfos: originInfos
    }

    var originPopupTemplate = new PopupTemplate({
        title: "Origin: {origin}"
    })

    maps.origin.featureLayer.renderer = originRenderer;
    maps.origin.featureLayer.popupTemplate = originPopupTemplate;

    maps.origin.map.add(maps.origin.featureLayer);



    // console.log('Hello');

    // [departmentColors, originColors].forEach(arr => {
    //     for (var i=0; i<colors.length; i++){

    //     }
    // });

});