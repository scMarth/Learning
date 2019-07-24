function getODPQueryLink(query){
    console.log(query);
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
    console.log(searchQuery);
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

    for (var key in responseMap){
        regex = responseMap[key]['regExpr'];
        keyData = responseMap[key];

        var r = new RegExp(regex, 'ig');
        var found = text.match(r);
        if (found){
            // if the data associated with this match has links
            if (keyData.links){
                for (var linkKey in keyData.links){
                    if (returnResponse)
                        returnResponse += '<br><br>';
                    returnResponse += linkKey + ':';

                    urls = keyData.links[linkKey];
                    urls.forEach(function(url){
                        returnResponse += '<br><a href="' + url + '" target="_blank">' + url + '</a>';
                    })
                }
            }

            // if the data associated with this match has an ODP query string
            if (keyData.odpQueryString){
                if (returnResponse)
                    returnResponse += '<br><br>';
                let queryString = keyData.odpQueryString;
                returnResponse += 'Results on our Open Data Portal for ' + queryString + ':'
                    + '<br><a href="' + getODPQueryLink(queryString) + '" target="_blank">' + getODPQueryLink(queryString) + '</a>';
            }

            break;
        }
    }

    return returnResponse ? returnResponse : noMatchResponse;
}

function getCategoryListHTML(){
    categoryListHTML = '<ul class="convo__msg--list">';
    // iterate through all categories in app.cfg.CATEGORIES and add them to the bulletted list
    var sortedKeys = [];
    for (var key in app.cfg.RESPONSE_MAP){
        sortedKeys.push(key);
    }
    sortedKeys.sort();

    for (var i=0; i<sortedKeys.length; i++){
        categoryListHTML += '<li>' + sortedKeys[i] + '</li>';
    }

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