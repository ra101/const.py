"""A pure python implementation of constants."""

from const import PyConst



class Links(PyConst):
    GITHUB = "https://github.com/ra101"
    WEB = "https://ra101.github.io/"
    EMAIL = "ping@ra101.dev"

class Author(PyConst):
    NAME = "〈 RA 〉"
    WEB = Links.WEB
    LINKS = Links



print(f"\n{Links.GITHUB = }")
print(f"{Links.get('WEB') = }")
print(f"{Links['EMAIL'] = }")

print(f"\n{Author.values() = }")
print(f"\n{dict(Author) = }")

print("\nfor key in Author.LINKS.keys()")
for key in Author.LINKS.keys():
    print(f'\t {getattr(Author.LINKS, key) = }')

print('\n')

try:
    Links.WEB = 'any_new_value'
    raise TypeError('AttributeError should have raised on re-assignment.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')

try:
    del Links.WEB
    raise TypeError('AttributeError should have raised on deletion.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')

try:
    Links.WEB_2 = 'any_new_value'
    raise TypeError('AttributeError should have raised on new assignment.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')
