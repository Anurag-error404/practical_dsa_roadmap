# Expression Evaluator (T1)

*Part 2 — Linear Structures*

## Problem

`"3 + 4 * 2"` isn't evaluable by reading left to right without a structure for precedence.

## Objective

Convert infix → postfix using a stack, then evaluate the postfix expression.

---

**Input:** A string expression, e.g. `"3 + 4 * 2 - (1 + 5)"`. **Output:** The evaluated numeric result (and, as an intermediate step, the postfix form).

**Edge cases:**

- Unbalanced parentheses — should raise a clear parse error, not crash mid-evaluation
- Operator precedence including `^` (exponent, right-associative — different from `+`/`-`/`*`/`/`)
- Unary minus, e.g. `"-3 + 5"` vs. binary minus in `"5 - 3"`
- Division by zero
- Multi-digit numbers and decimals (`"12.5 + 3"`), and inputs with inconsistent spacing

**Suggested structure:**

```
expr-evaluator/
├── tokenizer.py           # splits string into tokens
├── infix_to_postfix.py    # shunting-yard or equivalent
├── evaluator.py           # evaluates postfix using a stack
└── tests/
    └── test_evaluator.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
