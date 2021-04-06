import pandas as pd
import json

with open('deck.txt', 'r') as deckfile:
    ass = deckfile.read()

ass = pd.DataFrame([x.split('	') for x in ass.split('\n')])

responses = list(ass[0])

calls = list(ass[1]) + list(ass[2]) + list(ass[3])

deck = {
    'name':'ass deck', 
    'description':'trol', 
    'watermark':'ass', 
    'calls':[
        {
            'text':card.split('____')
        } for card in calls if card != ''
    ],
    'responses':[
        {'text':[card]} for card in responses if card != ''
    ]
}

with open('deck.json', 'w') as deckfile:
    deckfile.write(json.dumps(deck, indent=2))