from random import choice, sample

famous_houses = [
  '🐺 Stark',
  '🐉 Targaryen',
  '🦌 Baratheon',
  '🦑 Greyjoy',
  '🦁 Lannister'
]

example = sample(famous_houses, 2)

print(f'Example: {example}')


# ----------------


from random import sample as samp

example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)

print('Example: ' + example[0] + ' ' + example[1])