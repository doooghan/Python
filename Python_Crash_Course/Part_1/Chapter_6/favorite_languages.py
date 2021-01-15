favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# print("Sarah's favorite language is " +
#       favorite_languages['sarah'].title() +
#       ".")

"""
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print()

for name in favorite_languages:
    print(name.title())

print()

for name in favorite_languages.keys():
    print(name.title())
"""


friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("\tHi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")
