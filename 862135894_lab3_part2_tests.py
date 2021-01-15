

tests = [ {'description': 'PINA: 0x00  => PORTC: 0x40',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
    'expected': [('PORTC',0x40)],
    },
    {'description': 'PINA: 0x0F  => PORTC: 0x3F',
    'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3F)],
    },
        {'description': 'PINA: 0x0A  => PORTC: 0x3E',
    'steps': [ {'inputs': [('PINA',0x0A)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3E)],
    },
    {'description': 'PINA: 0x07  => PORTC: 0x3C',
    'steps': [ {'inputs': [('PINA',0x07)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3C)],
    },
    {'description': 'PINA: 0x05  => PORTC: 0x38',
    'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 5 } ],
    'expected': [('PORTC',0x38)],
    },
     {'description': 'PINA: 0x03  => PORTC: 0x70',
    'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 5 } ],
    'expected': [('PORTC',0x70)],
    },
     {'description': 'PINA: 0x01  => PORTC: 0x60',
    'steps': [ {'inputs': [('PINA',0x01)], 'iterations': 5 } ],
    'expected': [('PORTC',0x60)],
    },



    ]
#watch = ['PORTC']

