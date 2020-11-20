#include "msp430G2553.h"

#define G_LED BIT6
#define R_LED BIT0
#define BTN1 BIT3

void main(void){
    WDTCTL = WDTPW + WDTHOLD; // disable watch dog timer
    DCOCTL = CALDCO_1MHZ;    // set internal oscillator at 1MHz
    BCSCTL1 = CALBC1_1MHZ;   // set internal oscillator at 1MHz

    P1DIR = 0xF7; // Set all as outputs

    P1OUT = 0x00;

    P1SEL &= ~(BIT3 | BIT6);

    long count = 0;
    int green_LED_on = 0;

    int buttonOneValue = 0;

    for(;;) {
        buttonOneValue = P1IN & BTN1;

        if (buttonOneValue == 0){
            P1OUT &= ~(R_LED);   // Disable = 0
        }else{
            P1OUT |= R_LED;      // Enable = 1
        }

        count += 1;

        if (count == 100000){
            if (green_LED_on == 1){
                P1OUT &= ~(G_LED);   // Disable = 0
                green_LED_on = 0;
            }else{
                P1OUT |= G_LED;      // Enable = 1
                green_LED_on = 1;
            }
            count = 0;
        }
    }
}
