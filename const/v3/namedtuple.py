"""An implementation of constants using NamedTuple."""

from collections import namedtuple

from const.utils import check_upper_snake_case
from const.utils import check_pascal_case

class ConstantMeta(type):

    _dict_methods = (
        '__iter__', '__getitem__', 'get', 'items', 'keys', 'values'
    )

    def __new__(mcls, name, bases, classdict):
        check_pascal_case(name, raise_error=True)

        if not bases:
            return super().__new__(mcls, name, bases, classdict)

        const_map = {
            k: v for k,v in classdict.items()
            if check_upper_snake_case(k)
        }
        NamedTupleClass = namedtuple(name, list(const_map.keys()))

        class NamedDictClass(NamedTupleClass):
            _member_map_ = const_map
            _member_names_ = list(const_map)

            def __new__(cls, **kwargs):
                cls.__creating_class__ = True
                cls.__name__ = name
                for method in mcls._dict_methods:
                    setattr(cls, method, getattr(cls._member_map_, method))
                cls.__getattr__ = cls._member_map_.__getitem__
                cls.values = cls._member_map_.values
                cls.keys = cls._member_map_.keys
                obj = super().__new__(cls, **kwargs)
                cls.__creating_class__ = False
                return obj

            def __setattr__(self, name, value):
                if self.__creating_class__:
                    return super().__setattr__(name, value)
                verb = 'Reassign'if name in self._member_map_ else 'Assign new'
                raise AttributeError(
                    f'Cannot {verb} {self.__class__.__name__}.{name} member.'
                )

            def __delattr__(self, name):
                if self.__creating_class__:
                    return super().__delattr__(name)

                raise AttributeError(
                    f'Cannot Delete {self.__class__.__name__}.{name} member.'
                )

        return NamedDictClass(**const_map)


class Constant(metaclass=ConstantMeta):
    pass

