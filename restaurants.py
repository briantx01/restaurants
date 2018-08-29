import random

restaurants = [
    'Blaze Pizza',
    'Buffalo Wild Wings',
    'Cafe Istanbul',
    'Cane Rosso',
    'Chipotle',
    'Fadis',
    'La Hacienda',
    'Hutchins',
    'Mi Cocina',
    'Macaroni Grill',
    'Piadas',
    'Raising Canes',
    'Rudys BBQ',
    'Schlotzkys',
    'Texas Kabob House',
    'Tight Ends',
    'Taverna Rossa',
    'Twin Peaks',
    'Platias',
    'Village Burger',
    'Wild Pitch',
    'Wingstop'
]
samples = random.sample(set(restaurants), 3)
print(samples)
