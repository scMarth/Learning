/*

Blink

Turns on an LED on for one second, then off for one second, repeatedly.

Explaining what the code will do.
Anything within /* *\/ or after // is ignored, and is a comment to yourself
on what the piece of code will do (a great reminder after creating tens or hundreds of sketches).

*/


// The format:
// int (an integer/number)
// led (name) = 13 (pin where LED is connected to) 
// ; (semicolons are needed after every line that you type out code, 
// except for setup(), loop(), and any other function (anything with () ).

int led = 13;   // L LED

// Void setup: code that runs once; setup your inputs and outputs.
void setup() {
   // Setup our output
   pinMode(led, OUTPUT);
}

// Void loop: runs over and over after setup
void loop() {

   // Turn the LED on (HIGH is “on” in the Arduino language)
   digitalWrite(led, HIGH);

   // Delay/wait for a second (1000 milliseconds = 1 second)
   delay(1000);

   // Turn the LED off (LOW is “off” in the Arduino language)
   digitalWrite(led, LOW);

   // Delay/wait for a second
   delay(1000);
}