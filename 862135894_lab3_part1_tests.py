

tests = [ {'description': 'PINA: 0x00 , PINB: 0x00 => PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00)], 'iterations': 5 } ],
    'expected': [('PORTC',0x00)],
    },
    {'description': 'PINA: 0xFF , PINB: 0xFF => PORTC: 0x10',
    'steps': [ {'inputs': [('PINA',0xFF),('PINB',0xFF)], 'iterations': 5 } ],
    'expected': [('PORTC',0x10)],
    },
        {'description': 'PINA: 0x3E , PINB: 0x01 => PORTC: 0x06',
    'steps': [ {'inputs': [('PINA',0x3E),('PINB',0x01)], 'iterations': 5 } ],
    'expected': [('PORTC',0x06)],
    },
    {'description': 'PINA: 0x03 , PINB: 0x03 => PORTC: 0x04',
    'steps': [ {'inputs': [('PINA',0x03),('PINB',0x03)], 'iterations': 5 } ],
    'expected': [('PORTC',0x04)],
    },


    ]
#watch = ['PORTC']

