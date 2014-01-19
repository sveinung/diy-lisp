# -*- coding: utf-8 -*-

from types import Environment
from types import LispError
from types import Lambda
from types import is_boolean, is_atom, is_symbol, is_list, is_lambda
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    return unparse(ast)

