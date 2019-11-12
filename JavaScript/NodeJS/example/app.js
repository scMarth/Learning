const EventEmitter = require('events');

const Logger = require('./logger');
const logger = new Logger();

// Register a listener
logger.on('messageLogged', (arg) => { // by convention, we use arg, e, or eventArg
    console.log('Listener called', arg);
});

/*
// The above is equivalent to:

logger.on('messageLogged', function(arg){
    console.log('Listener called', arg);
});
*/

logger.log('message');