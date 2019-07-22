var app = {};

app.cfg = {
    /*

    The initial prompt is shown when the page is loaded. A list of categories is then printed.

    */
    INITIAL_PROMPT: 'Hello, which of the following are you interested in?',
    CATEGORIES: [
        'Airport Influence Area',
        'Alisal',
        'Alisal District',
        'Alisal Vibrancy Plan',
        'Alternative Transportation',
        'Bench Mark',
        'Benchmark',
        'Bikes',
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
        'Open Data',
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
        [/(aia)/ig,
            {
                odpQueryString: 'airport influence area'
            }
        ],
        [/airport\s*-*\s*influence\s*-*\s*area/ig,
            {
                odpQueryString: 'airport influence area'
            }
        ],
        [/alisal\s*-*\s*district/ig,
            {
                odpQueryString: 'alisal district'
            }
        ],
        [/alisal\s*-*\s*vibrancy\s*-*\s*plan/ig,
            {
                odpQueryString: 'alisal vibrancy plan'
            }
        ],
        [/alternative\s*-*\s*transportation/ig,
            {
                odpQueryString: 'alternative transportation'
            }
        ],
        [/bench\s*-*\s*mark/ig,
            {
                odpQueryString: 'benchmark'
            }
        ],
        [/(bike(path|way|\s*-\splan|\s*-\sroute|)|bicycle)/ig,
            {
                odpQueryString: 'bike'
            }
        ],
        [/building/ig,
            {
                odpQueryString: 'building'
            }
        ],
        [/centerline/ig,
            {
                odpQueryString: 'centerline'
            }
        ],
        [/city\s*-*\s*of\s*-*\s*salinas\s*-*\s*boundary/ig,
            {
                odpQueryString: 'city of salinas boundary'
            }
        ],
        [/community\s*-*\s*center/ig,
            {
                odpQueryString: 'community center'
            }
        ],
        [/community\s*-*\s*centers/ig,
            {
                odpQueryString: 'community centers'
            }
        ],
        [/community\s*-*\s*development/ig,
            {
                odpQueryString: 'community development'
            }
        ],
        [/community\s*-*\s*services/ig,
            {
                odpQueryString: 'community services'
            }
        ],
        [/council\s*-*\s*districts/ig,
            {
                odpQueryString: 'council districts'
            }
        ],
        [/economic\s*-*\s*development/ig,
            {
                odpQueryString: 'economic development'
            }
        ],
        [/emergency\s*-*\s*response/ig,
            {
                odpQueryString: 'emergency response'
            }
        ],
        [/fema/ig,
            {
                odpQueryString: 'fema'
            }
        ],
        [/facilities/ig,
            {
                odpQueryString: 'facilities'
            }
        ],
        [/family\s*-*\s*center/ig,
            {
                odpQueryString: 'family center'
            }
        ],
        [/family\s*-*\s*resource\s*-*\s*center/ig,
            {
                odpQueryString: 'family resource center'
            }
        ],
        [/federal\s*-*\s*emergency\s*-*\s*management\s*-*\s*agency/ig,
            {
                odpQueryString: 'federal emergency management agency'
            }
        ],
        [/fire\s*-*\s*department/ig,
            {
                odpQueryString: 'fire department'
            }
        ],
        [/fire\s*-*\s*house/ig,
            {
                odpQueryString: 'fire house'
            }
        ],
        [/fire\s*-*\s*station/ig,
            {
                odpQueryString: 'fire station'
            }
        ],
        [/firefighter/ig,
            {
                odpQueryString: 'firefighter'
            }
        ],
        [/flood/ig,
            {
                odpQueryString: 'flood'
            }
        ],
        [/gps/ig,
            {
                odpQueryString: 'gps'
            }
        ],
        [/gps\s*-*\s*control\s*-*\s*network/ig,
            {
                odpQueryString: 'gps control network'
            }
        ],
        [/general\s*-*\s*plan/ig,
            {
                odpQueryString: 'general plan'
            }
        ],
        [/half\s*-*\s*mile/ig,
            {
                odpQueryString: 'half mile'
            }
        ],
        [/high\s*-*\s*performing\s*-*\s*government/ig,
            {
                odpQueryString: 'high performing government'
            }
        ],
        [/intersection\s*-*\s*counts/ig,
            {
                odpQueryString: 'intersection counts'
            }
        ],
        [/intersection[s]*/ig,
            {
                odpQueryString: 'intersection'
            }
        ],
        [/kpi/ig,
            {
                odpQueryString: 'kpi'
            }
        ],
        [/landmarks/ig,
            {
                odpQueryString: 'landmarks'
            }
        ],
        [/landuse/ig,
            {
                odpQueryString: 'landuse'
            }
        ],
        [/librar(y|ies)/ig,
            {
                odpQueryString: 'library'
            }
        ],
        [/monument/ig,
            {
                odpQueryString: 'monument'
            }
        ],
        [/nfhl/ig,
            {
                odpQueryString: 'nfhl'
            }
        ],
        [/ngs/ig,
            {
                odpQueryString: 'ngs'
            }
        ],
        [/ntmp/ig,
            {
                odpQueryString: 'ntmp'
            }
        ],
        [/national\s*-*\s*geodetic\s*-*\s*survey/ig,
            {
                odpQueryString: 'national geodetic survey'
            }
        ],
        [/neighborhood\s*-*\s*vibrancy/ig,
            {
                odpQueryString: 'neighborhood vibrancy'
            }
        ],
        [/((open\s*-*\s*data)|portal)/ig,
            {
                links: [
                    {
                        text: 'Open Data Portal Homepage',
                        link: 'https://cityofsalinas.opendatasoft.com/pages/homepage/'
                    }
                ]
            }
        ],
        [/open\s*-*\s*space/ig,
            {
                odpQueryString: 'open space'
            }
        ],
        [/parks\s*-*\s*and\s*-*\s*recreation/ig,
            {
                odpQueryString: 'parks and recreation'
            }
        ],
        [/planning/ig,
            {
                odpQueryString: 'planning'
            }
        ],
        [/planning\s*-*\s*and\s*-*\s*community\s*-*\s*engagement/ig,
            {
                odpQueryString: 'planning and community engagement'
            }
        ],
        [/police/ig,
            {
                odpQueryString: 'police'
            }
        ],
        [/public\s*-*\s*works/ig,
            {
                odpQueryString: 'public works'
            }
        ],
        [/quality\s*-*\s*of\s*-*\s*life/ig,
            {
                odpQueryString: 'quality of life'
            }
        ],
        [/recreation/ig,
            {
                odpQueryString: 'recreation'
            }
        ],
        [/recreation\s*-*\s*centers/ig,
            {
                odpQueryString: 'recreation centers'
            }
        ],
        [/road/ig,
            {
                odpQueryString: 'road'
            }
        ],
        [/roundabouts/ig,
            {
                odpQueryString: 'roundabouts'
            }
        ],
        [/safety/ig,
            {
                odpQueryString: 'safety'
            }
        ],
        [/salinas\s*-*\s*municipal\s*-*\s*airport/ig,
            {
                odpQueryString: 'salinas municipal airport'
            }
        ],
        [/space/ig,
            {
                odpQueryString: 'space'
            }
        ],
        [/speed\s*-*\s*bumps/ig,
            {
                odpQueryString: 'speed bumps'
            }
        ],
        [/survey[s]*/ig,
            {
                odpQueryString: 'survey'
            }
        ],
        [/traffic/ig,
            {
                odpQueryString: 'traffic'
            }
        ],
        [/transportation/ig,
            {
                odpQueryString: 'transportation'
            }
        ],
        [/transportation\s*-*\s*and\s*-*\s*infrastructure/ig,
            {
                odpQueryString: 'transportation and infrastructure'
            }
        ],
        [/urban\s*-*\s*design/ig,
            {
                odpQueryString: 'urban design'
            }
        ],
        [/vision\s*-*\s*salinas/ig,
            {
                odpQueryString: 'vision salinas'
            }
        ],
        [/walk/ig,
            {
                odpQueryString: 'walk'
            }
        ],
        [/water/ig,
            {
                odpQueryString: 'water'
            }
        ],
        [/youth\s*-*\s*centers/ig,
            {
                odpQueryString: 'youth centers'
            }
        ],
        [/zoning/ig,
            {
                odpQueryString: 'zoning'
            }
        ],
        [/alisal/ig,
            {
                odpQueryString: 'alisal'
            }
        ],
        [/fire/ig,
            {
                odpQueryString: 'fire'
            }
        ],
        [/park/ig,
            {
                odpQueryString: 'park'
            }
        ],
        [/salinas/ig,
            {
                odpQueryString: 'salinas',
                links: [
                    {
                        text: 'City of Salinas Homepage',
                        link: 'https://www.cityofsalinas.org/'
                    },
                    {
                        text: 'Storymaps',
                        link: 'https://giswebservices.ci.salinas.ca.us/storymaps/dashboard/'
                    }
                ]
            }
        ],
        [/open/ig,
            {
                odpQueryString: 'open'
            }
        ]
    ]
};

function getODPQueryLink(query){
    tokens = query.split(' ');
    url = 'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=';
    searchQuery = '';
    tokens.forEach(function(word){
        if (searchQuery){
            searchQuery += '+' + word;
        }else{
            searchQuery = word;
        }
    })
    return url + searchQuery;
}

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

    var noMatchResponse = "Sorry, I am unable to help you with this. Please try again.";  
    var returnResponse = "";

    for (var i=0; i<responseMap.length; i++){
        regexResponsePair = responseMap[i];

        regex = regexResponsePair[0];
        responseData = regexResponsePair[1];

        var found = text.match(regex);
        if (found){

            // if the responseData has links
            if (responseData.links){
                responseData.links.forEach(function(item){
                    if (returnResponse)
                        returnResponse += '<br><br>';
                    returnResponse += item.text + ':'
                        + '<br><a href="' + item.link + '" target="_blank">' + item.link + '</a>';
                })
            }

            // if the responseData  has an Open Data Portal query string
            if (responseData.odpQueryString){
                if (returnResponse)
                    returnResponse += '<br><br>';
                let queryString = responseData.odpQueryString;
                returnResponse += 'Results on our Open Data Portal for ' + queryString + ':'
                + '<br><a href="' + getODPQueryLink(queryString) + '" target="_blank">' + getODPQueryLink(queryString) + '</a>';
            }
            break;
        }
    }

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