# -*- coding: utf-8 -*-

"""Functions to expand branches."""

from . import constants
from . import language


def t_neg(signed_formula):
    """Expand a true negation."""
    formula = signed_formula["formula"]["operands"][0]
    return {
        "left": [language.sign_formula(constants.F, formula)],
        "right": [],
    }


def f_neg(signed_formula):
    """Expand a false negation."""
    formula = signed_formula["formula"]["operands"][0]
    return {
        "left": [language.sign_formula(constants.T, formula)],
        "right": [],
    }


def t_conj(signed_formula):
    """Expand a true conjunction."""
    formula_1 = signed_formula["formula"]["operands"][0]
    formula_2 = signed_formula["formula"]["operands"][1]
    return {
        "left": [
            language.sign_formula(constants.T, formula_1),
            language.sign_formula(constants.T, formula_2),
        ],
        "right": [],
    }


def f_conj(signed_formula):
    """Expand a false conjunction."""
    formula_1 = signed_formula["formula"]["operands"][0]
    formula_2 = signed_formula["formula"]["operands"][1]
    return {
        "left": [language.sign_formula(constants.F, formula_1)],
        "right": [language.sign_formula(constants.F, formula_2)],
    }


def transformer(sign, operator):
    """Get the function that will do the expansion."""
    return rules[(sign, operator)]


rules = {
    (constants.T, constants.NEG): t_neg,
    (constants.F, constants.NEG): f_neg,
    (constants.T, constants.CONJ): t_conj,
    (constants.F, constants.CONJ): f_conj,
}
"""Map signs and operators to the appropriate transformation functions."""