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

To construct an atomic formula, use the ``atom()`` function::

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

To sign formulas, use the ``sign_formula()`` function. It takes two
arguments: (i) a value to sign it with like "T" or "F", and (ii) the
formula to sign::

    from inc.lib import language

    p = language.atom("P")
    true_p = language.sign_formula("T", p)

    neg_p = language.molecule("NEG", [p])
    false_neg_p = language.sign_formula("F", neg_p)


Running the Prover
------------------

Suppose we want to prove "P" from "P & Q". First, construct the formulas::

    from inc.lib import language
    p = language.atom("P")
    q = language.atom("Q")
    conj = language.molecule("CONJ", [p, q])

Sign the premises as true, and the conclusion as false::

    true_conj = language.sign_formula("T", conj)
    false_p = language.sign_formula("F", p)

Now import the ``main`` package, and the ``logics.PC`` module (this latter module has the propositional calculus tableaux rules)::

    from inc.lib import main
    from inc.lib.logics import PC

Now use the ``prove()`` function to run the prover. It takes two arguments: (i) a set of rules from the ``lib.logics`` package, and (ii) a list of signed formulas::

    success, incon, branches = main.prove(PC.rules, [true_conj, false_p])

The ``prove()`` function returns three items:

* Whether or not the proof succeeded.
* All inconsistent pairs of formulas on all expanded branches.
* All expanded branches.


Running mbC Proofs
------------------

Proofs for mbC are executed the same way, but use the ``logics.mbC.rules``.

Also, with mbC, you can construct ball formulas::

    from inc.lib import language
    from inc.lib import main
    from inc.lib.logics import mbC

    p = language.atom("P")
    ball_p = language.molecule("BALL", [p])
    neg_p = language.mocelule("NEG", [p])

    true_ball_p = language.sign_formula("T", ball_p)
    true_neg_p = language.sign_formula("T", neg_p)
    t_p = language.sign_formula("T", p)

    formulas = [true_ball_p, true_neg_p, t_p]
    success, incon, branches = main.prove(mbC.rules, formulas)


New Tableaux Rules
------------------

To add more tableaux rules, create a python file in the ``inc.lib.logics``
package. The file needs to have a ``rules`` variable that defines
the rules. Look at ``inc.lib.logics.PC.py`` as a template.