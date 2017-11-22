# -*- coding: utf-8 -*-

"""A module with utils for building formulas."""


def atom(operand):
    """Build a representation of an atomic formula."""
    return {"operator": None, "operands": [operand]}


def molecule(operator, operands):
    """Build a representation of a molecular formula."""
    return {"operator": operator, "operands": operands}


def sign_formula(sign, formula):
    """Build a representation of a signed formula."""
    return {"sign": sign, "formula": formula}
