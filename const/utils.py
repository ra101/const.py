
import re

_CLASS_RE_CONSTANT = re.compile(r'^[A-Z][A-Za-z0-9]*$')
_VAR_RE_CONSTANT = re.compile(r'^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$')


def check_pascal_case(name, raise_error=False):
    if _CLASS_RE_CONSTANT.fullmatch(name):
        return True
    if raise_error:
        raise ValueError(f'{name} is not a valid PascalCase.')


def check_upper_snake_case(name, raise_error=False):
    if _VAR_RE_CONSTANT.fullmatch(name):
        return True
    if raise_error:
        raise ValueError(f'{name} is not a valid UPPER_SNAKE_CASE.')
