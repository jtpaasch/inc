# -*- coding: utf-8 -*_

"""PC (propositional calculus) rules."""


rules = [

    {
        "input": [
            {
                "sign": "T",
                "formula": {
                    "operator": "NEG",
                    "operands": ["A"],
                }
            },
        ],
        "output": {
            "left": [
                {
                    "sign": "F",
                    "formula": {
                        "operator": None,
                        "operands": ["A"],
                    },
                },
            ],
            "right": [],
        },
    },

    {
        "input": [
            {
                "sign": "F",
                "formula": {
                    "operator": "NEG",
                    "operands": ["A"],
                },
            },
        ],
        "output": {
            "left": [
                {
                    "sign": "T",
                    "formula": {
                        "operator": None,
                        "operands": ["A"],
                    },
                },
            ],
            "right": [],
        },
    },

    {
        "input": [
            {
                "sign": "T",
                "formula": {
                    "operator": "CONJ",
                    "operands": ["A", "B"],
                },
            }
        ],
        "output": {
            "left": [
                {
                    "sign": "T",
                    "formula": {
                        "operator": None,
                        "operands": ["A"],
                    },
                },
                {
                    "sign": "T",
                    "formula": {
                        "operator": None,
                        "operands": ["B"],
                    },
                },
            ],
            "right": [],
        },
    },

    {
        "input": [
            {
                "sign": "F",
                "formula": {
                    "operator": "CONJ",
                    "operands": ["A", "B"],
                },
            },
        ],
        "output": {
            "left": [
                {
                    "sign": "F",
                    "formula": {
                        "operator": None,
                        "operands": ["A"],
                    },
                },
            ],
            "right": [
                {
                    "sign": "F",
                    "formula": {
                        "operator": None,
                        "operands": ["B"],
                    },
                },
            ],
        },
    },

]
