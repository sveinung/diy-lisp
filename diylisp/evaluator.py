# -*- coding: utf-8 -*-

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
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
    elif ast[0] == "define":
        define(ast, env)
    else:
        return env.lookup(ast)

def atom(exp, env):
    return not is_list(evaluate(exp, env))

def do_math(ast, operator, env):
    first = evaluate(ast[1], env)
    second = evaluate(ast[2], env)
    if not is_integer(first) or not is_integer(second):
        raise LispError
    return operator(first, second)

def do_if(ast, env):
    if evaluate(ast[1], env):
        return evaluate(ast[2], env)
    else:
        return evaluate(ast[3], env)

def define(ast, env):
    if len(ast) != 3:
        raise LispError("Wrong number of arguments")

    variable_name = ast[1]
    variable_value = ast[2]

    if not is_symbol(variable_name):
        raise LispError("non-symbol")

    env.set(variable_name, variable_value)

