
import re
import sys
from inspect import ast, getmembers

_CLASS_RE_CONSTANT = re.compile(r'^[A-Z][A-Za-z0-9]*$')
_VAR_RE_CONSTANT = re.compile(r'^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$')
_DUNDER_RE_CONSTANT = re.compile(r'^__\w+__$')


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


def check_dunder_case(name, raise_error=False):
    if _DUNDER_RE_CONSTANT.fullmatch(name):
        return True
    if raise_error:
        raise ValueError(f'{name} is not a valid UPPER_SNAKE_CASE.')


def constantize_module(name):

    const_module = sys.modules[name]

    # If the file is already converted to constant module.
    if not getattr(const_module, '__file__', None):
        return

    with open(const_module.__file__, 'r') as f:
        ast_tree = ast.parse(f.read())

    all_attrs = dict(getmembers(const_module))
    constant_attrs = dict()

    for node in ast.walk(ast_tree):

        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if node.name in all_attrs:
                constant_attrs[node.name] = all_attrs[node.name]

        elif isinstance(node, ast.Assign):
            constant_attrs.update({
                target.id: all_attrs[target.id]
                for target in node.targets if (
                    isinstance(target, ast.Name) and target.id) in all_attrs
            })

    from const import ConstModule

    sys.modules[name] = type(ConstModule)(
        name, (ConstModule, ), constant_attrs
    )


