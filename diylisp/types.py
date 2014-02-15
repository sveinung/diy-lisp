# -*- coding: utf-8 -*-

"""
This module holds some types we'll have use for along the way.

It's your job to implement the Closure and Environment types.
The LispError class you can have for free :)
"""

class LispError(Exception): 
    """General lisp error class."""
    pass

class Closure:
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
