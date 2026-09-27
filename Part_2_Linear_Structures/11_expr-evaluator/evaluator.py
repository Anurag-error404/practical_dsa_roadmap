"""Evaluates postfix using a stack."""
from infix_to_postfix import to_postfix
from tokenizer import tokenize


def eval_postfix(postfix: list[str]) -> float:
    """Evaluate postfix tokens with a stack."""
    raise NotImplementedError


def evaluate(expr: str) -> float:
    return eval_postfix(to_postfix(tokenize(expr)))
