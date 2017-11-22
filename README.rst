Inc
===

A tableaux theorem prover for mbC (a formally inconsistent logic).

It also has rules for PC (propositional calculus).


Installation
------------

Clone the repo somewhere, for instance::

    mkdir -p ~/code
    cd ~/code
    git clone https://github.com/jtpaasch/inc.git

Create a virtual environment::

    cd inc
    python -m venv venv
    . venv/bin/activate

Install tox::

    pip install tox

And install the package::

    pip install --editable .


Quality
-------

From the root of the repo, run tox::

    tox

This will run the unittests, and print a coverage report.


Constructing Formulas
---------------------

Construct an atomic formula::

    from inc.lib import language
    p = language.atom("P")

To construct a molecular formula, use the ``molecule()`` function. 
It takes two arguments: (i) a name for the operator, and (ii) a
list of operands. For instance, to make a conjunction::

    from inc.lib import language
    p = language.atom("P")
    q = language.atom("Q")
    conj = langauge.molecule("CONJ", [p, q])

Here is a negation (which is a unary operator, so it takes only one operand)::

    from inc.lib import language
    p = language.atom("P")
    neg_p = language.molecule("NEG", [p])

To sign formulas::

    from inc.lib import language

    p = language.atom("P")
    true_p = language.sign_formula("T", p)

    neg_p = language.molecule("NEG", [p])
    false_neg_p = language.sign_formula("F", neg_p)


Proving
-------

Suppose we want to prove "P" from "P & Q". First, construct the formulas::

    from inc.lib import language
    p = language.atom("P")
    q = language.atom("Q")
    conj = language.molecule("CONJ", [p, q])

Sign the premises as true and sign the conclusion as false::

    true_conj = language.sign_formula("T", conj)
    false_p = language.sign_formula("F", p)

Now prove that set of formulas, using the PC (propositional calculus) rules::

    from inc.lib import main
    from inc.lib.logics import PC
    success, inconsistencies, branches = main.prove(PC.rules, [true_conj, false_p])

The first returned item is whether the proof succeeded. 
The second returned item is a list of all inconsistent pairs
found on each expanded branch.
The third returned item is the list of expanded branches.


New Tableaux Rules
------------------

To add more tableaux rules, create a python file in the ``inc.lib.logics``
package. The file needs to have a ``rules`` variable that defines
the rules. Look at ``inc.lib.logics.PC.py`` as a template.