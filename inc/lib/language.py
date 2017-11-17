# -*- coding: utf-8 -*-

"""A module with utils for building formulas."""

from . import constants


def atom(formula):
    """Build a representation of an atomic formula."""
    return {"operator": None, "operands": [formula]}


def ball(formula):
    """Build a representation of a ball."""
    return {"operator": constants.BALL, "operands": [formula]}


def neg(formula):
    """Build a representation of a negation."""
    return {"operator": constants.NEG, "operands": [formula]}


def conj(formula_1, formula_2):
    """Build a representation of a conjunction."""
    return {"operator": constants.CONJ, "operands": [formula_1, formula_2]}


def sign_formula(sign, formula):
    """Build a representation of a signed formula."""
    return {"sign": sign, "formula": formula}
