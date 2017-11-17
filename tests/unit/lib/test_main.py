"""Unit tests for the ``lib.main`` module."""

from unittest import TestCase

from inc.lib import constants
from inc.lib import language
from inc.lib import main


class TestMain(TestCase):
    """Test suite for the ``lib.main`` module."""

    def test_run(self):
        """A dummy test."""
        output = []
        main.run(output.append)
        self.assertTrue(True)

    def test_get_inconsistencies(self):
        """Ensure ``get_inconsistencies()`` finds the inconsistencies."""
        atom = language.atom("A")
        true_atom = language.sign_formula(constants.T, atom)
        false_atom = language.sign_formula(constants.F, atom)

        atom_2 = language.atom("B")
        true_atom_2 = language.sign_formula(constants.T, atom_2)

        branch = [true_atom, false_atom, true_atom_2]

        result = main.get_inconsistencies(branch)
        expected = [(true_atom, false_atom)]
        self.assertEqual(result, expected)

    def test_resolve_only_atoms(self):
        """Ensure ``resolve()`` handles all atomic formulas."""
        atom_1 = language.atom("A")
        atom_2 = language.atom("B")
        true_atom_1 = language.sign_formula(constants.T, atom_1)
        false_atom_2 = language.sign_formula(constants.F, atom_2)

        branches = [[true_atom_1, false_atom_2]]
        expected = [[true_atom_1, false_atom_2]]

        result = main.resolve(branches)
        self.assertEqual(result, expected)

    def test_resolve_t_neg(self):
        """Ensure ``resolve()`` resolves true negations."""
        atom = language.atom("A")
        neg = language.neg(atom)
        true_neg = language.sign_formula(constants.T, neg)
        false_atom = language.sign_formula(constants.F, atom)

        branches = [[true_neg]]

        result = main.resolve(branches)
        self.assertEqual(result, [[false_atom]])

    def test_resolve_f_neg(self):
        """Ensure ``resolve()`` resolves false negations."""
        atom = language.atom("A")
        neg = language.neg(atom)
        false_neg = language.sign_formula(constants.F, neg)
        true_atom = language.sign_formula(constants.T, atom)

        branches = [[false_neg]]

        result = main.resolve(branches)
        self.assertEqual(result, [[true_atom]])

    def test_resolve_t_conj(self):
        """Ensure ``resolve()`` resolves true conjunctions."""
        atom_1 = language.atom("A")
        atom_2 = language.atom("B")
        conj = language.conj(atom_1, atom_2)
        true_conj = language.sign_formula(constants.T, conj)
        true_atom_1 = language.sign_formula(constants.T, atom_1)
        true_atom_2 = language.sign_formula(constants.T, atom_2)

        branches = [[true_conj]]

        result = main.resolve(branches)
        self.assertEqual(result, [[true_atom_1, true_atom_2]])

    def test_resolve_f_conj(self):
        """Ensure ``resolve()`` resolves false conjunctions."""
        atom_1 = language.atom("A")
        atom_2 = language.atom("B")
        conj = language.conj(atom_1, atom_2)
        false_conj = language.sign_formula(constants.F, conj)
        false_atom_1 = language.sign_formula(constants.F, atom_1)
        false_atom_2 = language.sign_formula(constants.F, atom_2)

        branches = [[false_conj]]

        result = main.resolve(branches)
        self.assertEqual(result, [[false_atom_1], [false_atom_2]])

    def test_resolve_modus_ponens(self):
        """Ensure ``resolve()`` resolves modus ponens."""
        atom_1 = language.atom("A")
        atom_2 = language.atom("B")
        neg_atom_2 = language.neg(atom_2)
        conj = language.conj(atom_1, neg_atom_2)
        false_conj = language.sign_formula(constants.F, conj)
        true_atom_1 = language.sign_formula(constants.T, atom_1)
        false_atom_1 = language.sign_formula(constants.F, atom_1)
        true_atom_2 = language.sign_formula(constants.T, atom_2)
        false_atom_2 = language.sign_formula(constants.F, atom_2)

        branches = [[true_atom_1, false_conj, false_atom_2]]
        expected = [
            [true_atom_1, false_atom_2, false_atom_1],
            [true_atom_1, false_atom_2, true_atom_2],
        ]

        result = main.resolve(branches)
        self.assertEqual(result, expected)
