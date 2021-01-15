/*	Partner(s) Name & E-mail:none
 *	Lab Section: 22
 *	Assignment: Lab # 3 Exercise # 1
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
	DDRA = 0x00; PORTA = 0xFF; 
	DDRB = 0x00; PORTB = 0xFF; 
	DDRC = 0xFF; PORTC = 0x00; 

	
	unsigned char tmpA = 0x00;
	unsigned char tmpB = 0x00;
	unsigned char tmpC = 0x00;
	
	
while(1) {
	
		tmpA = PINA;
		tmpB = PINB;
		tmpC = 0x00;
		
		for(unsigned i = 0; i<8; i++){
			if(tmpA & (1<<i))tmpC++;
			
			if(tmpB & (1<<i))tmpC++;
		}
		


PORTC = tmpC;	

	}
	return 0;
}

