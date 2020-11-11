#include "msp430G2553.h"

void main(void)
{
    WDTCTL = WDTPW + WDTHOLD;

    // P1.0 (Red LED)
    P1DIR |= BIT0;

    // P1.3 (Push Button S2)
    P1DIR &= ~BIT3;
    P1REN |= BIT3;
    P1OUT |= BIT3; // enable the pullup resistor

    P1OUT &= ~BIT0; // turn off the LED

    while(1)
    {
        if((P1IN & BIT3) != BIT3)
        {

            // wait for the button to be released
            while((P1IN & BIT3) != BIT3){
                continue;
            }

            // toggle the LED
            if ((P1OUT & BIT0) == BIT0){
                // if the LED is on, turn it off
                P1OUT &= ~BIT0;
            }else{
                // if the LED is off, turn it on
                P1OUT |= BIT0;
            }
        }
    }
}
