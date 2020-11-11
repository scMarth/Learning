/*

toggle the red LED when the push button is pressed

https://embeddedprojecthunter.wordpress.com/2015/08/28/simple-button-programming-for-msp430g2553/

*/


#include "msp430G2553.h"

void main(void)
{
    WDTCTL = WDTPW + WDTHOLD; // turn off watchdog timer


    /*

    P1DIR –> Port 1 Direction
    This line of code simply make P1.0 as the output pin. So what happen to the other unassigned pin such as P1.1, P1.2 and so on? Well, it will automatically assigned as input. Thus, in this case, P1.3 is auto-assigned as input too.

    */
    P1DIR = BIT0;

    /*

    P1REN –> Port 1 Resistor Enable
    P1.3 is connected to the button. In order to make the button work, we have to add pull-up resistor to make it normally high.

    By writing this line, internal resistor (inside the chip) will be enabled, connecting P1.3 to the power supply (3.6V) or ground (0V). This is defined in next line.

    The details on the working principle of button will be discussed in next session.

    */
    P1REN = BIT3;



    /*

    P1OUT –> Port 1 Output
    Although P1OUT means setting the output state. But, if we analyse carefully, P1.3 is an input pin, and it is quite not logical to assign the pin any output state. In fact, this line of code define the connectivity of the internal resistor. If P1OUT = BIT3, then the internal resistor is connected to 3.6V. In other words, the pin now is normally high, and the internal resistor is known as pull-up resistor. Else, if P1OUT &= ~BIT3, then the internal resistor is connected to ground, and it is known as pull-down resistor. Details will be discussed in later session.

    */
    P1OUT = BIT3;

    while(1)
    {
        if((P1IN & BIT3)!=BIT3)
        {
            __delay_cycles(220000);
            P1OUT ^= BIT0;
        }
    }
}
