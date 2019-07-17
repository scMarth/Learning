var app = {};

app.cfg = {
    /*

    The initial prompt is shown when the page is loaded. A list of categories is then printed.

    */
    INITIAL_PROMPT: 'Hello, which of the following did you need help with?',
    CATEGORIES: [
        'Change password',
        'Change e-mail'
    ],

    /*
    
    A resposne map in the form of an array. Each item in the response map is a list, which contains a pairing of a
    regular expression which will be searched in the user's input, and a string containing what text should be displayed
    to the user when that regular expression is matched.

    */
    RESPONSE_MAP: [
        [/[Ee]\s*-*\s*[Mm][Aa][Ii][Ll]/g, "You want to change your email"],
        [/[Pp][Aa][Ss][Ss]\s*-*\s*[Ww][Oo][Rr][Dd]/g, "You want to change your password"]
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
        response = regexResponsePair[1];

        var found = text.match(regex);
        if (found){
            returnResponse = response;
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