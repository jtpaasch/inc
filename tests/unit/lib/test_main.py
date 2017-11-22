"""Unit tests for the ``lib.main`` module."""

from unittest import TestCase

from inc.lib import language
from inc.lib import main

from inc.lib.logics import mbC, PC


class TestMain(TestCase):
    """Test suite for the ``lib.main`` module."""

    def test_run(self):
        """A dummy test."""
        output = []
        main.run(output.append)
        self.assertTrue(True)

    def test_expand_t_neg_PC(self):
        """Ensure ``expand()`` expands false negations (for PC)."""
        a = language.atom("A")
        neg_a = language.molecule("NEG", [a])
        t_neg_a = language.sign_formula("T", neg_a)
        f_a = language.sign_formula("F", a)

        branches = [[t_neg_a]]

        result = main.expand(PC.rules, branches)
        self.assertEqual(result, [[f_a]])

    def test_expand_t_neg_mbC(self):
        """Ensure ``expand()`` expands false negations (for mbC)."""
        a = language.atom("A")
        neg_a = language.molecule("NEG", [a])
        ball_a = language.molecule("BALL", [a])
        f_a = language.sign_formula("F", a)
        t_neg_a = language.sign_formula("T", neg_a)
        t_ball_a = language.sign_formula("T", ball_a)

        branches = [[t_neg_a, t_ball_a]]

        result = main.expand(mbC.rules, branches)
        self.assertEqual(result, [[f_a]])

    def test_expand_f_neg(self):
        """Ensure ``expand()`` expands false negations."""
        a = language.atom("A")
        neg_a = language.molecule("NEG", [a])
        f_neg_a = language.sign_formula("F", neg_a)
        t_a = language.sign_formula("T", a)

        branches = [[f_neg_a]]

        result = main.expand(PC.rules, branches)
        self.assertEqual(result, [[t_a]])

    def test_expand_t_conj(self):
        """Ensure ``expand()`` expands true conjunctions."""
        a = language.atom("A")
        b = language.atom("B")
        conj = language.molecule("CONJ", [a, b])
        t_conj = language.sign_formula("T", conj)
        t_a = language.sign_formula("T", a)
        t_b = language.sign_formula("T", b)

        branches = [[t_conj]]

        result = main.expand(PC.rules, branches)
        self.assertEqual(result, [[t_a, t_b]])

    def test_expand_f_conj(self):
        """Ensure ``expand()`` expands false conjunctions."""
        a = language.atom("A")
        b = language.atom("B")
        conj = language.molecule("CONJ", [a, b])
        f_conj = language.sign_formula("F", conj)
        f_a = language.sign_formula("F", a)
        f_b = language.sign_formula("F", b)

        branches = [[f_conj]]

        result = main.expand(PC.rules, branches)
        self.assertEqual(result, [[f_a], [f_b]])

    def test_prove_modus_ponens(self):
        """Ensure ``prove()`` proves modus ponens."""
        a = language.atom("A")
        b = language.atom("B")
        neg_b = language.molecule("NEG", [b])
        conj = language.molecule("CONJ", [a, neg_b])
        f_conj = language.sign_formula("F", conj)
        t_a = language.sign_formula("T", a)
        f_a = language.sign_formula("F", a)
        t_b = language.sign_formula("T", b)
        f_b = language.sign_formula("F", b)

        result = main.prove(PC.rules, [t_a, f_conj, f_b])

        expected = (
            True,
            [[(t_a, f_a)], [(f_b, t_b)]],
            [[t_a, f_b, f_a], [t_a, f_b, t_b]])
        self.assertEqual(result, expected)

    def test_prove_explosion(self):
        """Ensure ``prove()`` proves explosion."""
        a = language.atom("A")
        b = language.atom("B")
        t_a = language.sign_formula("T", a)
        f_a = language.sign_formula("F", a)
        f_b = language.sign_formula("F", b)

        result = main.prove(PC.rules, [t_a, f_a, f_b])

        expected = (
            True,
            [[(t_a, f_a)]],
            [[t_a, f_a, f_b]])
        self.assertEqual(result, expected)

    def test_prove_nothing(self):
        """Ensure ``prove()`` doesn't prove non-sequiturs."""
        a = language.atom("A")
        b = language.atom("B")
        t_a = language.sign_formula("T", a)
        f_b = language.sign_formula("F", b)

        result = main.prove(PC.rules, [t_a, f_b])

        expected = (
            False,
            [[]],
            [[t_a, f_b]])
        self.assertEqual(result, expected)
