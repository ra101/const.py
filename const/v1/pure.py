"""A pure python implementation of constants."""


class ConstantMeta(type):
    """
    Meta Class for Constant, How Constant class would behave
    """

    def __new__(mcls, name, bases, classdict):
        """
        adding __keys__, __values__ fields
        and keys(), values() methods.
        """
        classdict['__creating_class__'] = True
        cls = super().__new__(mcls, name, bases, classdict)

        __values__, __keys__ = [], []
        for key, val in vars(cls).items():
            if not key.startswith("__"):
                __values__.append(val)
                __keys__.append(key)
        cls.__keys__ = tuple(__keys__)
        cls.__values__ = tuple(__values__)
        cls.keys =  lambda: cls.__keys__
        cls.values = lambda: cls.__values__

        del cls.__creating_class__
        return cls

    def __setattr__(cls, name, value):
        if hasattr(cls, '__creating_class__'):
            return super().__setattr__(name, value)

        verb = 'Reassign' if name in cls.__keys__ else 'Assign new'
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

    def get(cls, key, default=None):
        if key in cls.__keys__:
            return getattr(cls, key)
        return default


class Constant(metaclass=ConstantMeta):
    """
    Now this class can be inherited whenever required to make constants
    """
    pass
