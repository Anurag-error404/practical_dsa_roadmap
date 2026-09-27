import pytest

from tokenizer import ParseError, tokenize
from infix_to_postfix import to_postfix
from evaluator import eval_postfix, evaluate


def test_unbalanced_parentheses_raise_parse_error():
    # TODO: Unbalanced parentheses — should raise a clear parse error, not crash mid-evaluation
    ...


def test_exponent_precedence_is_right_associative():
    # TODO: Operator precedence including `^` (exponent, right-associative — different from
    #       `+`/`-`/`*`/`/`)
    ...


def test_unary_minus_vs_binary_minus():
    # TODO: Unary minus, e.g. `"-3 + 5"` vs. binary minus in `"5 - 3"`
    ...


def test_division_by_zero():
    # TODO: Division by zero
    ...


def test_multi_digit_decimals_and_irregular_spacing():
    # TODO: Multi-digit numbers and decimals (`"12.5 + 3"`), and inputs with inconsistent
    #       spacing
    ...
