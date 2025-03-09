"""An implementation of constants using NamedTuple."""

from types import ModuleType
from types import MappingProxyType

from const.utils import check_dunder_case


class ConstantModuleMeta(type):

    _dict_methods = (
        '__iter__', '__getitem__', 'get',
        'items', 'keys', 'values'
    )

    def __new__(mcls, name, bases, classdict):

        if not bases:
            return super().__new__(mcls, name, bases, classdict)

        const_map = {
            k: v for k,v in classdict.items()
            if not check_dunder_case(k)
        }


        PopulatedModuleType = type(
            'PopulatedModuleType', (ModuleType, ), const_map
        )

        class ConstantModuleClass(PopulatedModuleType):
            _member_map_ = MappingProxyType(const_map)

            def __new__(cls, bases):
                for method in mcls._dict_methods:
                    setattr(cls, method, getattr(cls._member_map_, method))
                return super().__new__(cls, bases)


            def __setattr__(self, name, value):
                verb = 'Reassign'if name in self._member_map_ else 'Assign new'
                raise AttributeError(
                    f'Cannot {verb} {self.__name__}.{name} member.'
                )

            def __delattr__(self, name):
                raise AttributeError(
                    f'Cannot Delete {self.__name__}.{name} member.'
                )

        return ConstantModuleClass(name)


class ConstantModule(metaclass=ConstantModuleMeta):
    pass
