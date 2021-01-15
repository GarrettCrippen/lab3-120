/*	Partner(s) Name & E-mail:none
 *	Lab Section: 22
 *	Assignment: Lab # 3 Exercise # 3
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
	DDRB = 0xFF; PORTB = 0x00; 
	DDRC = 0xFF; PORTC = 0x00; 

	
	unsigned char tmpA = 0x00;
	unsigned char tmpA2 = 0x00;

	
	
while(1) {
	
		tmpA = (PINA & 0x0F)<<4;
		tmpA2 = (PINA & 0xF0)>>4;

		
		
		
PORTB = (PORTB & 0xF0) |tmpA2;	
PORTC = (PORTC & 0x0F) |tmpA;	


	}
	return 0;
}

