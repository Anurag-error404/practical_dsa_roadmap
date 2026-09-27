import pytest

from models import Item
from comparator import build_comparator, sort_items
from external_sort import external_sort


def test_primary_ties_broken_by_secondary_and_tertiary():
    # TODO: Ties on the primary key that need the secondary (and tertiary) key to break
    #       correctly
    ...


def test_conflicting_or_duplicate_sort_keys():
    # TODO: User specifies a conflicting or duplicate key in the sort order
    ...


def test_missing_attribute_sort_position():
    # TODO: Missing attribute values on some items (e.g., a file with no modified-date) — decide
    #       where these sort (first, last, or excluded)
    ...


def test_external_sort_for_input_larger_than_memory():
    # TODO: A file list large enough it doesn't fit in memory — needs an external sort (chunk,
    #       sort each chunk, merge from disk)
    ...
