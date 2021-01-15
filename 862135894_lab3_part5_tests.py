

tests = [ {'description': 'PIND: 0x00 ,  PINB:0x00 => PORTB: 0x00',
    'steps': [ {'inputs': [('PIND',0x00),('PINB',0x00)], 'iterations': 5 } ],
    'expected': [('PORTB',0x00)],
    },
    {'description': 'PIND: 0x04 ,  PINB:0x00 => PORTB: 0x04',
    'steps': [ {'inputs': [('PIND',0x04),('PINB',0x00)], 'iterations': 5 } ],
    'expected': [('PORTB',0x04)],
    },
      {'description': 'PIND: 0xFF ,  PINB:0x00 => PORTB: 0x02',
    'steps': [ {'inputs': [('PIND',0xFF),('PINB',0x00)], 'iterations': 5 } ],
    'expected': [('PORTB',0x02)],
    },
    {'description': 'PIND: 0xFF ,  PINB:0x01 => PORTB: 0x02',
    'steps': [ {'inputs': [('PIND',0xFF),('PINB',0x01)], 'iterations': 5 } ],
    'expected': [('PORTB',0x02)],
    },
    

    ]
#watch = ['PORTB']

