import pytest

from parser import parse_timestamp
from merger import merge_logs
from validator import check_sorted


def test_unsorted_input_file_is_flagged():
    # TODO: A file that isn't actually sorted internally — should be detected and flagged, not
    #       silently merged wrong
    ...


def test_merge_streams_without_loading_whole_files():
    # TODO: Files large enough that none can be fully loaded into memory — needs a true k-way
    #       merge (read line-by-line, min-heap of "next line per file"), not "load everything,
    #       then sort"
    ...


def test_duplicate_timestamps_tie_breaking():
    # TODO: Duplicate timestamps across files — decide tie-breaking order (e.g., preserve file
    #       order as a secondary key)
    ...


def test_empty_file_and_single_file_input():
    # TODO: An empty input file, or a file list of size 1
    ...
