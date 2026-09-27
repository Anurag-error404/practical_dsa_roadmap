import pytest

from models import Product, Bundle
from category_tree import CategoryNode, CategoryTree
from product_store import ProductStore
from filter_sort import filter_by_price, sort_products
from bundle_optimizer import suggest_bundle
from catalogue import Catalogue


def test_empty_category_returns_empty():
    # TODO: A category with no products — empty result, not an error
    ...


def test_price_filter_min_greater_than_max_rejected():
    # TODO: A price filter where min > max — invalid input, reject explicitly
    ...


def test_sort_by_missing_field_null_position():
    # TODO: Sorting by a field some products are missing — decide where nulls sort (first, last,
    #       or excluded) and be consistent
    ...


def test_no_bundle_fits_budget_empty_with_message():
    # TODO: A bundle request where no combination fits the budget — return an empty bundle with
    #       a clear message, not an error
    ...


def test_product_in_multiple_categories_model():
    # TODO: A product belonging to multiple categories — decide whether the category structure
    #       is a strict tree (one parent) or a more general graph, since this changes your data
    #       model entirely
    ...
