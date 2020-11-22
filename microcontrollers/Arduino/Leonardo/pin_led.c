/*

Set pin 2 to an input and turn on the pullup resistor so that it goes high unless connected to ground.
Tie the L LED (pin 13) to the negation of pin 2. If you connect pin 2 to ground via physical wire, the LED turns on.
Otherwise, the LED remains off.

*/

int led = 13;   // L LED

// Void setup: code that runs once; setup your inputs and outputs.
void setup() {
   // Setup our output
   pinMode(led, OUTPUT);
   pinMode(2, INPUT_PULLUP);
}

// Void loop: runs over and over after setup
void loop() {
  digitalWrite(led, !digitalRead(2));
}