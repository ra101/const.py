from const import ConstModule


class Author(ConstModule):
    NAME = "〈 RA 〉"

    class Links:
        GITHUB = "https://github.com/ra101"
        WEB = "https://ra101.dev/"
        EMAIL = "ping@ra101.dev"

    WEB = Links.WEB


print(f"\n{Author = }")

print(f"\n{Author.Links.GITHUB = }")
print(f"{Author.get('WEB') = }")
print(f"{Author['NAME'] = }")

print(f"\n{Author.values() = }")
print(f"\n{dict(Author) = }")

print("\nfor key in Author.LINKS.keys()")
for key in Author.keys():
    print(f'\t {getattr(Author, key) = }')

print('\n')

try:
    Author.NAME = 'any_new_value'
    raise TypeError('AttributeError should have raised on re-assignment.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')

try:
    del Author.NAME
    raise TypeError('AttributeError should have raised on deletion.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')

try:
    Author.NAME_1 = 'any_new_value'
    raise TypeError('AttributeError should have raised on new assignment.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')