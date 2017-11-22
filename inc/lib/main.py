# -*- coding: utf-8 -*-

"""The main module for the lib."""

from copy import deepcopy
from itertools import combinations


def is_match(schema, formula):
    """Check if a formula is an instance of a schema."""
    conditions = (
        schema["sign"] == formula["sign"],
        schema["formula"]["operator"] == formula["formula"]["operator"])
    return all(conditions)


def get_match(schema, branch):
    """Find an instance of a schema on a branch."""
    matches = [x for x in branch if is_match(schema, x)]
    return matches[0] if matches else None


def get_matches(rule, branch):
    """Find all instances of schemas on a branch."""
    matches = [get_match(schema, branch) for schema in rule["input"]]
    non_empty_matches = [x for x in matches if x]
    return non_empty_matches


def remove_formulas(formulas, branch):
    """Remove formulas from a branch."""
    for formula in formulas:
        branch.remove(formula)
    return branch


def get_replacements(rule, matches):
    """Make a dict of operands to replace placeholders in rule schema."""
    replacements = {}
    for schema in rule["input"]:
        for match in matches:
            schema_operands = schema["formula"]["operands"]
            match_operands = match["formula"]["operands"]
            for i in range(len(schema_operands)):
                replacements[schema_operands[i]] = match_operands[i]
    return replacements


def get_new_formula(schema, replacements):
    """Generate a new formula by replacing placeholders in a schema."""
    result = {"sign": schema["sign"], "formula": {}}
    operator = schema["formula"]["operator"]
    operands = []
    for operand in schema["formula"]["operands"]:
        operands.append(replacements[operand])
    if operator is None:
        result["formula"] = operands[0]
    else:
        result["formula"] = {"operator": operator, "operands": operands}
    return result


def get_leaves(rule, matches):
    """Get new leaves from formulas that match the rule's schema."""
    result = {"left": [], "right": []}
    replacements = get_replacements(rule, matches)
    for side in ["left", "right"]:
        for schema in rule["output"][side]:
            formula = get_new_formula(schema, replacements)
            result[side].append(formula)
    return result


def expand(rules, branches):
    """Expand all branches, given a set of expansion rules."""
    result = []
    while branches:
        branch = branches[0]
        branches.remove(branch)

        do_again = True
        while do_again:
            do_again = False

            for rule in rules:
                matches = get_matches(rule, branch)

                if matches:
                    do_again = True
                    branch = remove_formulas(matches, branch)
                    leaves = get_leaves(rule, matches)

                    if leaves["right"]:
                        new_branch = deepcopy(branch)
                        new_branch.extend(leaves["right"])
                        branches.append(new_branch)

                    if leaves["left"]:
                        branch.extend(leaves["left"])

        result.append(branch)
    return result


def is_inconsistent(pair):
    """Determine if a pair of signed formulas are inconsistent."""
    conditions = (
        pair[0]["formula"]["operands"] == pair[1]["formula"]["operands"],
        pair[0]["formula"]["operator"] == pair[1]["formula"]["operator"],
        pair[0]["sign"] != pair[1]["sign"])
    return all(conditions)


def get_inconsistencies(branch):
    """Get all pairs of inconsistent formulas on a branch."""
    pairs = combinations(branch, 2)
    return [x for x in pairs if is_inconsistent(x)]


def prove(rules, signed_formulas):
    """Prove that a list of signed formulas are inconsistent."""
    branches = [signed_formulas]
    expanded_branches = expand(rules, branches)

    inconsistencies = []
    for branch in expanded_branches:
        inconsistent_pairs = get_inconsistencies(branch)
        inconsistencies.append(inconsistent_pairs)

    inconsistent_branches = [True for x in inconsistencies if x]
    success = len(inconsistent_branches) == len(expanded_branches)
    return success, inconsistencies, expanded_branches


def run(log):
    log("Hello world.")
