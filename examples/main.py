from examples import constants


try:
    constants.Links = 'any_new_value'
    raise TypeError('AttributeError should have raised on re-assignment.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')

try:
    del constants.Links
    raise TypeError('AttributeError should have raised on deletion.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')

try:
    constants.Links = 'any_new_value'
    raise TypeError('AttributeError should have raised on new assignment.')
except AttributeError as e:
    print(f'AttributeError raised with message: \"{e}\"')
