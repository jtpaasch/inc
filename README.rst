# Inc

Finds inconsistencies in a set of formulas.


## About

Does a tableaux proof, but without negating the formula to be proved.


## Installation

Clone the repo somewhere, for instance:

    mkdir -p ~/code
    cd ~/code
    git clone https://github.com/jtpaasch/inc.git

Create a virtual environment:

    cd inc
    python -m venv venv
    . venv/bin/activate

Install tox:

    pip install tox

And install the package:

    pip install --editable .


## Quality

From the root of the repo, run tox:

    tox

This will run the unittests, and print a coverage report.


## Run the program

To execute the program, from the project's repo, with the virtual
environment activated, try this:

    inc --help

That will display the help.
