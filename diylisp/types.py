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
        self.variables = variables if variables else {}

    def set(self, symbol, value):
        print self.variables
        if symbol in self.variables:
            raise LispError("already defined")

        self.variables[symbol] = value

    def extend(self, variables):
        copiedVariables = self.variables.copy()
        copiedVariables.update(variables)
        return Environment(copiedVariables)

    def lookup(self, symbol):
        if symbol not in self.variables:
            raise LispError(symbol)

        return self.variables[symbol]

    def __str__(self):
        return str(self.variables)

class LispError(Exception): 
    pass

