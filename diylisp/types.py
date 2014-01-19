# -*- coding: utf-8 -*-

def is_symbol(x):
    return isinstance(x, str)

def is_list(x):
    return isinstance(x, list)

def is_boolean(x):
    return isinstance(x, bool)

def is_integer(x):
    return isinstance(x, int)

def is_lambda(x):
    return isinstance(x, Lambda)

def is_atom(x):
    return is_symbol(x) \
        or is_integer(x) \
        or is_boolean(x) \
        or is_lambda(x)

class Lambda:
    def __init__(self, params, body, env):
        raise LispError("DIY")

    def __str__(self):
        raise LispError("DIY")

class Environment:
    def __init__(self, variables=None):
        pass
        # DIY

    def set(self, symbol, value):
        if symbol in self.bindings:
            raise LispError("Variable '%s' is already defined." % symbol)
        self.bindings[symbol] = value

    def extend(self, variables):
        raise LispError("DIY")

    def lookup(self, symbol):
        raise LispError("DIY")

class LispError(Exception): 
    pass

