# -*- coding: utf-8 -*-

"""The main module for the lib."""

import copy
from itertools import combinations

from . import constants
from . import transforms


def next_molecule(branch):
    """Get the next molecular formula in a list of formulas."""
    for signed_formula in branch:
        if signed_formula["formula"]["operator"] is not None:
            return signed_formula


def has_molecules(branch):
    """Check if a branch has any molecules."""
    molecules = [x for x in branch if x.get("operator")]
    return len(molecules) > 0


def is_inconsistent(pair):
    """Check if a pair of signed formulas are inconsistent."""
    conditions = [
        pair[0]["formula"]["operands"] == pair[1]["formula"]["operands"],
        pair[0]["formula"]["operator"] == pair[1]["formula"]["operator"],
        pair[0]["sign"] != pair[1]["sign"],
    ]
    return all(conditions)


def get_inconsistencies(branch):
    """Find all inconsistent atomic formulas in a branch."""
    pairs = combinations(branch, 2)
    return [x for x in pairs if is_inconsistent(x)]


def expand(signed_formula):
    """Expand a formula."""
    sign = signed_formula["sign"]
    formula = signed_formula["formula"]
    operator = formula["operator"]
    transform_func = transforms.transformer(sign, operator)
    return transform_func(signed_formula)


def resolve(branches):
    """Resolve all branches to atomic formulas."""
    result = []
    while branches:

        branch = branches[0]
        branches.remove(branch)

        count = 0
        do_again = True
        while do_again and count < constants.MAX_ITERATIONS:
            count = count + 1

            molecule = next_molecule(branch)
            if molecule:

                branch.remove(molecule)
                leaves = expand(molecule)

                if leaves["right"]:
                    new_branch = copy.deepcopy(branch)
                    new_branch.extend(leaves["right"])
                    branches.append(new_branch)

                branch.extend(leaves["left"])

            do_again = has_molecules(branch)

        result.append(branch)

    return result


def run(log):
    log("Hello world.")
