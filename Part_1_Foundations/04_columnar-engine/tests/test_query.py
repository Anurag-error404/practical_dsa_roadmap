import pytest

from loader import load_csv
from store import ColumnStore
from query import col_sum, col_avg, col_filter


def test_null_values_policy_in_aggregates():
    # TODO: Column contains missing/null values — decide whether they're skipped or zero-filled
    #       in aggregates
    ...


def test_unknown_column_raises_clear_error():
    # TODO: Query references a column name that doesn't exist — clear error, not a silent `None`
    ...


def test_empty_dataset_sum_zero_avg_undefined():
    # TODO: Empty dataset — `sum` should return 0, `avg` should error or return `None` (division
    #       by zero)
    ...


def test_dirty_numeric_column_fails_at_load_time():
    # TODO: A numeric column containing one stray non-numeric value (dirty data) — fail loudly
    #       at load time, not silently at query time
    ...
