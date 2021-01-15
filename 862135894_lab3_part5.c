/*	Partner(s) Name & E-mail:none
 *	Lab Section: 22
 *	Assignment: Lab # 3 Exercise # 5
 *	Exercise Description: [optional - include for your own benefit]
 *	
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */

#include <avr/io.h>
#ifdef _SIMULATE_
#include <../header/simAVRHeader.h>
#endif	

int main(void) {
	DDRD = 0x00; PORTD = 0xFF; 
	DDRB = 0xFF; PORTB = 0xFF; 


	
	unsigned char tmpD = 0x00;
	unsigned char tmpB = 0x00;
	unsigned short val = 0x00;
	
	
while(1) {
		tmpD = PIND;
		tmpB = PINB;
		val = tmpD;
		val = val<<1 | tmpB;
		
		
		if(val>=70){tmpB=0x02;}
		else if(val>5){tmpB=0x04;}
		else{tmpB=(tmpB&0xF8);}

	PORTB = tmpB;
	}
	return 0;
}

