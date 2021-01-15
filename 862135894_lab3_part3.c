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
	DDRC = 0xFF; PORTC = 0x00; 

	
	unsigned char tmpA = 0x00;
	unsigned char tmpA2 = 0x00;
	unsigned char tmpC = 0x00;
	
	
while(1) {
	
		tmpA = PINA&0xF;
		tmpA2 = PINA&0x70;
		tmpC = 0x00;
		
		
		if(tmpA>=13) tmpC = tmpC | 1<<0;
		if(tmpA>=10) tmpC = tmpC | 1<<1;
		if(tmpA>=7) tmpC = tmpC | 1<<2;
		if(tmpA>=5) tmpC = tmpC | 1<<3;
		if(tmpA>=3) tmpC = tmpC | 1<<4;
		if(tmpA>=1) tmpC = tmpC | 1<<5; 
		
		if(tmpA<=4)tmpC = tmpC| 1<<6;
		
		if((tmpA2&0x10) &&(tmpA2&0x20)&& !(tmpA2&0x40))tmpC = tmpC | 1<<7;
		
		
		

PORTC = tmpC;	

	}
	return 0;
}

