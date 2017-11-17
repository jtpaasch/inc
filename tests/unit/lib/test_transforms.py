"""Unit tests for the ``lib.transforms`` module."""

from unittest import TestCase

from inc.lib import constants
from inc.lib import language
from inc.lib import transforms


class TestTransforms(TestCase):
    """Test suite for the ``lib.transforms`` module."""

    def test_t_neg(self):
        """Ensure ``t_neg()`` produces the right leaves."""
        atom = language.atom("dummy-formula")
        signed_atom = language.sign_formula(constants.F, atom)

        formula = language.neg(atom)
        signed_formula = language.sign_formula(constants.T, formula)

        result = transforms.t_neg(signed_formula)
        expected = {"left": [signed_atom], "right": []}
        self.assertEqual(result, expected)

    def test_f_neg(self):
        """Ensure ``f_neg()`` produces the right leaves."""
        atom = language.atom("dummy-formula")
        signed_atom = language.sign_formula(constants.T, atom)

        formula = language.neg(atom)
        signed_formula = language.sign_formula(constants.F, formula)

        result = transforms.f_neg(signed_formula)
        expected = {"left": [signed_atom], "right": []}
        self.assertEqual(result, expected)

    def test_t_conj(self):
        """Ensure ``t_conj()`` produces the right leaves."""
        atom_1 = language.atom("dummy-formula-1")
        signed_atom_1 = language.sign_formula(constants.T, atom_1)
        atom_2 = language.atom("dummy-formula-2")
        signed_atom_2 = language.sign_formula(constants.T, atom_2)

        formula = language.conj(atom_1, atom_2)
        signed_formula = language.sign_formula(constants.T, formula)

        result = transforms.t_conj(signed_formula)
        expected = {"left": [signed_atom_1, signed_atom_2], "right": []}
        self.assertEqual(result, expected)

    def test_f_conj(self):
        """Ensure ``f_conj()`` produces the right leaves."""
        atom_1 = language.atom("dummy-formula-1")
        signed_atom_1 = language.sign_formula(constants.F, atom_1)
        atom_2 = language.atom("dummy-formula-2")
        signed_atom_2 = language.sign_formula(constants.F, atom_2)

        formula = language.conj(atom_1, atom_2)
        signed_formula = language.sign_formula(constants.F, formula)

        result = transforms.f_conj(signed_formula)
        expected = {"left": [signed_atom_1], "right": [signed_atom_2]}
        self.assertEqual(result, expected)

    def test_transformer(self):
        """Ensure ``transformer()`` returns mapped functions."""
        result = transforms.transformer(constants.T, constants.NEG)
        expected = transforms.t_neg
        self.assertEqual(result, expected)
