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
    elif ast[0] == "lambda":
        return closure(ast, env)
    elif ast[0] == "cons":
        return cons(ast, env)
    elif is_closure(ast[0]):
        return evaluate_closure(ast, env)
    elif is_list(ast):
        return evaluate_function(ast, env)
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
    variable_value = evaluate(ast[2], env)

    if not is_symbol(variable_name):
        raise LispError("non-symbol")

    env.set(variable_name, variable_value)

def closure(ast, env):
    if len(ast) != 3:
        raise LispError("number of arguments")

    return Closure(ast[1], ast[2], env)

def cons(ast, env):
    if evaluate(ast[2], env) == "nil":
        tail = []
    else:
        tail = evaluate(ast[2], env)
    return [evaluate(ast[1], env)] + tail

def evaluate_closure(ast, env):
    closure = ast[0]
    arguments = [evaluate(argument, env) for argument in ast[1:]]

    actual = len(arguments)
    expected = len(closure.params)
    if actual != expected:
        raise LispError("wrong number of arguments, expected " + str(expected) + " got " + str(actual))

    closure_assignments = dict(zip(closure.params, arguments))
    closure_assignments_with_closure_env = closure.env.extend(closure_assignments)

    return evaluate(closure.body, env.extend(closure_assignments_with_closure_env.variables))

def evaluate_function(ast, env):
    if is_list(ast[0]):
        function = evaluate(ast[0], env)
        return do_function(function, ast, env)
    elif ast[0] in env.variables:
        function = env.lookup(ast[0])
        return do_function(function, ast, env)
    else:
        raise LispError("not a function")

def do_function(function, ast, env):
    return evaluate([function] + ast[1:], env)
