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
    }
}

function showInitialPrompt(){
    printAiMsg('Hello, what do you want help with?');
}

// Process the input whenever the user presses enter after typing an input
document.querySelector('#convo-container > .reply-box > .reply-box__input-box > input').addEventListener('keydown', function onEvent(event){
    if (event.key === 'Enter'){
        processInput();
    }
});

showInitialPrompt();