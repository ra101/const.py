"""An implementation of constants using MappingProxyType."""

from types import MappingProxyType

from const.utils import check_upper_snake_case
from const.utils import check_pascal_case


class ConstantMeta(type):
    """
    Meta Class for Constant, How Constant class would behave
    """

    _dict_methods = (
        '__iter__', '__getitem__', 'get', 'items', 'keys', 'values'
    )


    def __new__(mcls, name, bases, classdict):
        """
        adding __keys__, __values__ fields
        and keys(), values() methods.
        """
        check_pascal_case(name, raise_error=True)

        if not bases:
            return super().__new__(mcls, name, bases, classdict)

        classdict['__creating_class__'] = True
        obj = super().__new__(mcls, name, bases, classdict)


        obj._mapping_proxy_ = MappingProxyType({
            k: v for k,v in vars(obj).items()
            if check_upper_snake_case(k)
        })

        for method in mcls._dict_methods:
            setattr(obj, method, getattr(obj._mapping_proxy_, method))

        del obj.__creating_class__
        return obj

    def __setattr__(cls, name, value):
        if hasattr(cls, '__creating_class__'):
            return super().__setattr__(name, value)

        verb = 'Reassign' if name in cls._mapping_proxy_ else 'Assign new'
        raise AttributeError(
            f'Cannot {verb} {cls.__name__}.{name} member.'
        )

    def __delattr__(cls, name):
        if hasattr(cls, '__creating_class__'):
            return super().__delattr__(name)

        raise AttributeError(
            f'Cannot Delete {cls.__name__}.{name} member.'
        )

    def __getitem__(cls, key):
        """adding __getitem__ to make objects `subscriptable`"""
        value =  getattr(cls, key)
        return value

    def __iter__(cls):
        """Override set for making loops work"""
        return zip(cls.__keys__, cls.__values__)


class Constant(metaclass=ConstantMeta):
    """
    Now this class can be inherited whenever required to make constants
    """

    pass

