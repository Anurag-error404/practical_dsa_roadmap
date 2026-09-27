import pytest

from reverse import reverse
from palindrome import is_palindrome
from anagram import is_anagram
from compress import rle_compress


def test_empty_and_single_char_are_palindromes():
    # TODO: Empty string and single-character string — both are trivially palindromes
    ...


def test_case_sensitivity_policy_documented():
    # TODO: Case sensitivity — decide and document whether `"Race car"` counts as a palindrome
    ...


def test_unicode_reversed_by_character_not_byte():
    # TODO: Unicode/multi-byte characters — reversing byte-by-byte vs. character-by-character
    #       gives different (wrong) results for some scripts
    ...


def test_compression_keeps_original_when_no_benefit():
    # TODO: Compression that would expand the string (e.g., `"abcdef"` under naive run-length
    #       encoding) — handle the "no benefit, keep original" case
    ...
