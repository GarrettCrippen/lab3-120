

tests = [ {'description': 'PINA: 0x00  => PORTB: 0x00, PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
    'expected': [('PORTB',0x00),('PORTC',0x00)],
    },
    {'description': 'PINA: 0x40  => PORTB: 0x04, PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0x40)], 'iterations': 5 } ],
    'expected': [('PORTB',0x04),('PORTC',0x00)],
    },
    {'description': 'PINA: 0x04  => PORTB: 0x00, PORTC: 0x40',
    'steps': [ {'inputs': [('PINA',0x04)], 'iterations': 5 } ],
    'expected': [('PORTB',0x00),('PORTC',0x40)],
    },
    {'description': 'PINA: 0x34  => PORTB: 0x03, PORTC: 0x40',
    'steps': [ {'inputs': [('PINA',0x34)], 'iterations': 5 } ],
    'expected': [('PORTB',0x03),('PORTC',0x40)],
    },

    ]
#watch = ['PORTC','PORTB']

