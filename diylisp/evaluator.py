# -*- coding: utf-8 -*-

from types import Environment
from types import LispError
from types import Lambda
from types import is_boolean, is_atom, is_symbol, is_list, is_lambda, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse
import operator as op

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    if is_integer(ast):
        return ast
    elif ast[0] == "quote":
        return ast[1]
    elif ast[0] == "atom":
        return atom(ast[1], env)
    elif ast[0] == "eq":
        first = evaluate(ast[1], env)
        second = evaluate(ast[2], env)
        return first == second
    elif ast[0] == "+":
        return do_math(ast, op.add, env)
    elif ast[0] == "-":
        return do_math(ast, op.sub, env)
    elif ast[0] == "/":
        return do_math(ast, op.div, env)
    elif ast[0] == "*":
        return do_math(ast, op.mul, env)
    elif ast[0] == "mod":
        return do_math(ast, op.mod, env)
    elif ast[0] == ">":
        return do_math(ast, op.gt, env)
    elif ast[0] == "if":
        return do_if(ast, env)
    else:
        raise NotImplementedError(ast)

def atom(exp, env):
    return not is_list(evaluate(exp, env))

def do_math(ast, operator, env):
    return operator(evaluate(ast[1], env), evaluate(ast[2], env))

def do_if(ast, env):
    if evaluate(ast[1], env):
        return evaluate(ast[2], env)
    else:
        return evaluate(ast[3], env)
