const EventEmitter = require('events');

var url = 'http://mylogger.io/log';

class Logger extends EventEmitter {
    // when you define a function in a class, you don't need the function keyword
    log(message){
        // Send an HTTP request
        console.log(message);
    
        // Raise an event
        /*
    
        We first give the name of the event we want to emit. Then, we can pass
        some data. It's good practice to encapsulate the event argument in an
        object where the data is labeled. 
    
        */
        this.emit('messageLogged', { id: 1, url: 'http://'});
    }
}



module.exports = Logger;