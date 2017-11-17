"""Unit tests for the ``lib.language`` module."""

from unittest import TestCase

from inc.lib import constants
from inc.lib import language


class TestLanguage(TestCase):
    """Test suite for the ``lib.language`` module."""

    def test_atom(self):
        """Ensure ``neg()`` builds the right representation of an atom."""
        formula = "dummy-formula"
        result = language.atom(formula)
        expected = {"operator": None, "operands": [formula]}
        self.assertEqual(result, expected)

    def test_ball(self):
        """Ensure ``ball()`` builds the right representation af a ball."""
        formula = language.atom("dummy-formula")
        result = language.ball(formula)
        expected = {"operator": constants.BALL, "operands": [formula]}
        self.assertEqual(result, expected)

    def test_neg(self):
        """Ensure ``neg()`` builds the right representation of a negation."""
        formula = language.atom("dummy-formula")
        result = language.neg(formula)
        expected = {"operator": constants.NEG, "operands": [formula]}
        self.assertEqual(result, expected)

    def test_conj(self):
        """Ensure ``conj()`` builds the right representation of a conj."""
        formula_1 = language.atom("dummy-formula-1")
        formula_2 = language.atom("dummy-formula-2")
        conj = [formula_1, formula_2]
        result = language.conj(*conj)
        expected = {"operator": constants.CONJ, "operands": conj}
        self.assertEqual(result, expected)

    def test_sign_formula(self):
        """Ensure ``sign_formula()`` builds a correct signed representation."""
        formula = language.atom("dummy-formula")
        result = language.sign_formula(constants.T, formula)
        expected = {"sign": constants.T, "formula": formula}
        self.assertEqual(result, expected)
