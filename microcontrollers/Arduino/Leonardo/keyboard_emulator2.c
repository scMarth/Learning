#include <Keyboard.h>
#include <time.h>

int led = 13;     // L LED

void setup() {
   // make pin 2 an input and turn on the
   // pullup resistor so it goes high unless
   // connected to ground:
   pinMode(2, INPUT_PULLUP);
   pinMode(3, INPUT_PULLUP);
   pinMode(4, INPUT_PULLUP);
   pinMode(led, OUTPUT);
   Keyboard.begin();
   srand(time(NULL));   // Initialization, should only be called once.
}

void loop() {
   digitalWrite(led, !(digitalRead(2)||digitalRead(4)));

   if (digitalRead(2) == HIGH && digitalRead(3) == HIGH && digitalRead(4) == LOW){
      // print random letter
      int r = rand() % 94;
      r += 32;
      Keyboard.print((char)r);
      delay(120); // 1 word ~ 5 chars, 500 chars per minute => 1 char per 60/500 seconds  ~ 120 milliseconds
   } else if (digitalRead(2) == HIGH && digitalRead(3) == LOW && digitalRead(4) == HIGH){
      // Keyboard.write(13); // send the "Enter" key // doesn't work
      Keyboard.write(KEY_RETURN); // send the "Enter" key
      delay(100);
   } else if (digitalRead(2) == LOW && digitalRead(3) == HIGH && digitalRead(4) == HIGH){
      Keyboard.print("q");
   }
}