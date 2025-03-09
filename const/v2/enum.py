"""An implementation of constants using Enum."""

from enum import Enum, EnumMeta

from const.utils import check_pascal_case
from const.utils import check_upper_snake_case


class ConstantMeta(EnumMeta):
    """
    Metaclass for fetching the value of the enum directly
    and making re-assignments invalid.
    Source: https://stackoverflow.com/a/54950492
    Source: https://stackoverflow.com/a/54333490
    """

    def __new__(mcls, name, bases, classdict):
        check_pascal_case(name, raise_error=True)
        classdict['__creating_class__'] = True
        enum = super().__new__(mcls, name, bases, classdict)
        for key in enum._member_names_:
            check_upper_snake_case(key, raise_error=True)
        del enum.__creating_class__
        return enum

    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value

    def __setattr__(cls, name, value):
        if hasattr(cls, '__creating_class__'):
            return super().__setattr__(name, value)

        verb = 'Reassign' if name in cls._member_map_ else 'Assign new'
        raise AttributeError(
            f'Cannot {verb} {cls.__name__}.{name} member.'
        )

    def __delattr__(cls, name):
        if hasattr(cls, '__creating_class__'):
            return super().__delattr__(name)

        raise AttributeError(
            f'Cannot Delete {cls.__name__}.{name} member.'
        )

    def __getitem__(cls, name):
        return getattr(cls, name)

    def __repr__(cls):
        return f'{cls.__name__}({cls._member_names_})'

    def keys(cls):
        return cls._member_map_.keys()

    def values(cls):
        return cls._member_map_.values()

    def get(cls, key, default=None):
        if key in cls._member_map_:
            return getattr(cls, key)
        return default


class Constant(Enum, metaclass=ConstantMeta):
    pass
