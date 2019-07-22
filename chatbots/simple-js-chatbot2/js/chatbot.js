var app = {};

app.cfg = {
    /*

    The initial prompt is shown when the page is loaded. A list of categories is then printed.

    */
    INITIAL_PROMPT: 'Hello, which of the following did you need help with?',
    CATEGORIES: [
        'Airport Influence Area',
        'Alisal',
        'Alisal District',
        'Alisal Vibrancy Plan',
        'Alternative Transportation',
        'Bench Mark',
        'Benchmark',
        'Bike',
        'Building',
        'Centerline',
        'City of Salinas Boundary',
        'Community Center',
        'Community Centers',
        'Community Development',
        'Community Services',
        'Council Districts',
        'Economic Development',
        'Emergency Response',
        'FEMA',
        'Facilities',
        'Family Center',
        'Family Resource Center',
        'Federal Emergency Management Agency',
        'Fire',
        'Fire Department',
        'Fire House',
        'Fire Station',
        'Firefighter',
        'Flood',
        'GPS',
        'GPS Control Network',
        'General Plan',
        'Half Mile',
        'High Performing Government',
        'Intersection Counts',
        'Intersections',
        'Intersections',
        'KPI',
        'Landmarks',
        'Landuse',
        'Library',
        'Monument',
        'NFHL',
        'NGS',
        'NTMP',
        'National Geodetic Survey',
        'Neighborhood Vibrancy',
        'Open',
        'Open Space',
        'Park',
        'Parks and Recreation',
        'Planning',
        'Planning and Community Engagement',
        'Police',
        'Public Works',
        'Quality of Life',
        'Recreation',
        'Recreation Centers',
        'Road',
        'Roundabouts',
        'Safety',
        'Salinas',
        'Salinas Municipal Airport',
        'Space',
        'Speed Bumps',
        'Survey',
        'Survey',
        'Traffic',
        'Transportation',
        'Transportation and Infrastructure',
        'Urban Design',
        'Vision Salinas',
        'Walk',
        'Water',
        'Youth Centers',
        'Zoning'
    ],

    /*
    
    A resposne map in the form of an array. Each item in the response map is a list, which contains a pairing of a
    regular expression which will be searched in the user's input, and a list of description and links

    */
    RESPONSE_MAP: [
        [/AIA/ig,
            [
                {
                    description: "Here are Airport Influence Area results from our Open Data Portal:",
                    link: "https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=airport+influence+area"
                }
            ]
        ],
        [/airport\s*-*\s*influence\s*-*\s*area/ig,
            [
                {
                    description: "Here are results from our Open Data Portal for 'Airport Influence Area':",
                    link: "https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=airport+influence+area"
                }
            ]
        ],
        [/alisal/ig,
            [
                {
                    description: "Here are results from our Open Data Portal for 'Alisal':",
                    link: "https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=alisal"
                }
            ]
        ],
        [/alisal\s*-*\s*district/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/alisal\s*-*\s*vibrancy\s*-*\s*plan/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/alternative\s*-*\s*transportation/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/bench\s*-*\s*mark/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/benchmark/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/(bike(path|way|\s*-*\s*plan|\s*-*\s*route)|bicycle)/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/building/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/centerline/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/city\s*-*\s*of\s*-*\s*salinas\s*-*\s*boundary/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/community\s*-*\s*center/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/community\s*-*\s*centers/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/community\s*-*\s*development/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/community\s*-*\s*services/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/council\s*-*\s*districts/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/economic\s*-*\s*development/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/emergency\s*-*\s*response/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/fema/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/facilities/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/family\s*-*\s*center/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/family\s*-*\s*resource\s*-*\s*center/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/federal\s*-*\s*emergency\s*-*\s*management\s*-*\s*agency/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/fire/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/fire\s*-*\s*department/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/fire\s*-*\s*house/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/fire\s*-*\s*station/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/firefighter/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/flood/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/gps/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/gps\s*-*\s*control\s*-*\s*network/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/general\s*-*\s*plan/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/half\s*-*\s*mile/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/high\s*-*\s*performing\s*-*\s*government/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/intersection\s*-*\s*counts/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/intersections/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/intersections/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/kpi/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/landmarks/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/landuse/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/library/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/monument/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/nfhl/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/ngs/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/ntmp/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/national\s*-*\s*geodetic\s*-*\s*survey/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/neighborhood\s*-*\s*vibrancy/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/open/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/open\s*-*\s*space/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/park/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/parks\s*-*\s*and\s*-*\s*recreation/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/planning/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/planning\s*-*\s*and\s*-*\s*community\s*-*\s*engagement/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/police/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/public\s*-*\s*works/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/quality\s*-*\s*of\s*-*\s*life/ig,
            [
                {
                    description: "Here are quality of life results from our Open Data Portal:",
                    link: "https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=quality+of+life"
                }
            ]
        ],
        [/recreation/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/recreation\s*-*\s*centers/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/road/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/roundabouts/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/safety/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/salinas/ig,
            [
                {
                    description: "Visit the City of Salinas website:",
                    link: "https://www.cityofsalinas.org/"
                },
                {
                    description: "Visit the City of Salinas Open Data Portal:",
                    link: "https://cityofsalinas.opendatasoft.com/pages/homepage/"
                },
                {
                    description: "Visit our storymaps:",
                    link: "https://giswebservices.ci.salinas.ca.us/storymaps/dashboard/"
                },
                {
                    description: "Visit the City of Salinas GIS Division webpage:",
                    link: "https://www.cityofsalinas.org/our-city-services/public-works/gis-services"
                },
                {
                    description: "View our map gallery:",
                    link: "https://www.cityofsalinas.org/our-government/information-center/map-gallery"
                }
            ]
        ],
        [/salinas\s*-*\s*municipal\s*-*\s*airport/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/space/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/speed\s*-*\s*bumps/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/survey/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/survey/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/traffic/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/transportation/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/transportation\s*-*\s*and\s*-*\s*infrastructure/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/urban\s*-*\s*design/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/vision\s*-*\s*salinas/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/walk/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/water/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/youth\s*-*\s*centers/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ],
        [/zoning/ig,
            [
                {
                    description: "",
                    link: ""
                }
            ]
        ]
    ]
};

function appendToConvoHistory(text){
    var output = document.querySelector('#convo-container > .convo');
    output.insertAdjacentHTML('beforeend', text);
}

function printAiMsg(message){
    var msg = '<div class="convo__msg-wrapper">'
        + '<div class="convo__msg convo__msg--ai">' + message
        + '</div></div>';
    appendToConvoHistory(msg);
}

function printUserMsg(message){
    var msg = '<div class="convo__msg-wrapper">'
        + '<div class="convo__msg convo__msg--user">' + message
        + '</div></div>';
    appendToConvoHistory(msg);
}

function clearReplyMsg(){
    document.querySelector('#convo-container > .reply-box > .reply-box__input-box > input').value = '';
}

// Processes the user's reply message, and adds the user's message to the conversation history
function processInput(){
    var input = document.querySelector('#convo-container > .reply-box > .reply-box__input-box > input').value;
    if (input){
        printUserMsg(input);
        clearReplyMsg();
        var aiResponse = fetchResponse(input);
        printAiMsg(aiResponse);
        scrollConvoHistory();
    }
}

function scrollConvoHistory(){
    convoDiv = document.querySelector('#convo-container > .convo');
    convoDiv.scrollTop = convoDiv.scrollHeight;

}

function fetchResponse(text){
    var responseMap = app.cfg.RESPONSE_MAP;

    var returnResponse = "Sorry, I am unable to help you with this. Here is a list of topics I can help you with:";
    returnResponse += '<br><br>' + getCategoryListHTML();


    responseMap.forEach(function(regexResponsePair){
        regex = regexResponsePair[0];
        responseData = regexResponsePair[1];

        var found = text.match(regex);
        if (found){
            returnResponse = '';
            responseData.forEach(function(responseItem){
                returnResponse += responseItem.description;
                    if (responseItem.link){
                        returnResponse += '<br><a href="' + responseItem.link + '" target="_blank">' + responseItem.link + '</a>'
                    }
                    returnResponse += '<br>';
            })
            return;
        }
    });

    return returnResponse;
}

function getCategoryListHTML(){
    categoryListHTML = '<ul class="convo__msg--list">';
    // iterate through all categories in app.cfg.CATEGORIES and add them to the bulletted list
    app.cfg.CATEGORIES.forEach(function(category){
        categoryListHTML += '<li>' + category + '</li>';
    });
    categoryListHTML += '</ul>';
    return categoryListHTML;
}

function showInitialPrompt(){
    printAiMsg(app.cfg.INITIAL_PROMPT + '<br><br>' + getCategoryListHTML());
}

// Process the input whenever the user presses enter after typing an input
document.querySelector('#convo-container > .reply-box > .reply-box__input-box > input').addEventListener('keydown', function onEvent(event){
    if (event.key === 'Enter'){
        processInput();
    }
});

showInitialPrompt();