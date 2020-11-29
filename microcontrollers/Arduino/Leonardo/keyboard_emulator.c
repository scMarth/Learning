

#include <Keyboard.h>

int led = 13;     // L LED

void setup() {
   // make pin 2 an input and turn on the
   // pullup resistor so it goes high unless
   // connected to ground:
   pinMode(2, INPUT_PULLUP);
   pinMode(led, OUTPUT);
   Keyboard.begin();
}

void loop() {
   digitalWrite(led, !digitalRead(2));
   //if the button is pressed
   if (digitalRead(2) == LOW) {
      //Send the message
      Keyboard.print("q");
   }
}

/*

Notes and Warnings

https://www.arduino.cc/reference/en/language/functions/usb/keyboard/keyboardprint/

When you use the Keyboard.print() command, the Arduino takes over your keyboard! Make sure you have control before you use the command. A pushbutton to toggle the keyboard control state is effective.

*/