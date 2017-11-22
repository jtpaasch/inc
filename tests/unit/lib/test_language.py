"""Unit tests for the ``lib.language`` module."""

from unittest import TestCase

from inc.lib import language


class TestLanguage(TestCase):
    """Test suite for the ``lib.language`` module."""

    def test_atom(self):
        """Ensure ``atom()`` builds the right representation."""
        operand = "dummy-proposition"
        result = language.atom(operand)
        expected = {"operator": None, "operands": [operand]}
        self.assertEqual(result, expected)

    def test_molecule(self):
        """Ensure ``molecule()`` builds the right representation."""
        operand_1 = "dummy-proposition-1"
        operand_2 = "dummy-proposition-2"
        operator = "dummy-operator"
        result = language.molecule(operator, [operand_1, operand_2])
        expected = {"operator": operator, "operands": [operand_1, operand_2]}
        self.assertEqual(result, expected)

    def test_sign_formula(self):
        """Ensure ``sign_formula()`` builds the right representation."""
        formula = language.atom("dummy-formula")
        result = language.sign_formula("T", formula)
        expected = {"sign": "T", "formula": formula}
        self.assertEqual(result, expected)
