// var questionNum = 0;                            // keep count of question, used for IF condition.
// var question = '<h1>Hello, what is your name?</h1>';   // first question

// var output = document.getElementById('output'); // store id="output" in output variable
// output.innerHTML = question;                    // ouput first question

// function bot() { 
//     var input = document.getElementById("input").value;
//     // console.log(input);

//     if (questionNum == 0) {
//         output.innerHTML = '<h1>hello ' + input + '</h1>';  // output response
//         document.getElementById("input").value = "";        // clear text box
//         question = '<h1>how old are you?</h1>';             // load next question       
//         setTimeout(timedQuestion, 2000);                    // output next question after 2sec delay
//     }

//     else if (questionNum == 1) {
//         var currYear = new Date().getFullYear();
//         output.innerHTML = '<h1>That means you were born in ' + (currYear - input) + '</h1>';
//         document.getElementById("input").value = "";
//         question = '<h1>where are you from?</h1>';
//         setTimeout(timedQuestion, 2000);
//     }
// }

// function timedQuestion() {
//     output.innerHTML = question;
// }

// //push enter key (using jquery), to run bot function.
// $(document).keypress(function(e) {
//   if (e.which == 13) {
//     bot();              // run bot function when enter key pressed
//     questionNum++;      // increase questionNum count by 1
//   }
// });

function appendToConvoHistory(text){
    var output = document.querySelector('#convo-container > .convo');
    output.insertAdjacentHTML('beforeend', output);
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

function processInput(){
    var input = document.querySelector('#convo-container > .reply-box > reply-box__input-box > input');


}

function showInitialPrompt(){
    printAiMsg('Hello, what do you want help with?');
}

showInitialPrompt();