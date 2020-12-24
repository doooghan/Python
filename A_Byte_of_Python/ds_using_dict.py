ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Swaroop']

print('\nThere are {} contacts in the address-bool\n'.format(len(ab)))

for key, value in ab.items():
    print('Contact {} at {}'.format(key, value))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is {}".format(ab['Guido']))

