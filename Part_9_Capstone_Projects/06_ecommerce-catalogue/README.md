# E-Commerce Catalogue Engine

*Type 3 — Capstones*

## Problem

Browsing a large catalogue needs hierarchy, filtering, sorting, and bundling — all fast, all at once.

## Objective

Build a catalogue with category browsing, price filtering, multi-key sorting, and value-optimized bundle suggestions.

---

**Combines:** Hashing · BST/Trees · Two Pointers/Sliding Window · Sorting · Knapsack DP

**Input:** A product catalogue (category, price, rating, etc.); `browse(category)`, `filter(price_range)`, `sort(criteria)`, `bundle_suggest(budget)`. **Output:** Filtered/sorted product list; a bundle recommendation within budget maximizing value.

**Edge cases:**

- A category with no products — empty result, not an error
- A price filter where min > max — invalid input, reject explicitly
- Sorting by a field some products are missing — decide where nulls sort (first, last, or excluded) and be consistent
- A bundle request where no combination fits the budget — return an empty bundle with a clear message, not an error
- A product belonging to multiple categories — decide whether the category structure is a strict tree (one parent) or a more general graph, since this changes your data model entirely

**Suggested structure:**

```
ecommerce-catalogue/
├── category_tree.py     # tree or graph, depending on multi-category decision
├── product_store.py     # hashing for product lookup
├── filter_sort.py       # two-pointer/sliding-window range filter + multi-key sort
├── bundle_optimizer.py  # knapsack-based bundle suggestion
└── tests/
    └── test_catalogue.py   # multi-category handling, no-fit bundle case
```

---

## Scaffold notes

- `models.py` holds the dataclasses shared across modules, so every module speaks the same types.
- Added `catalogue.py` as the single entry point for browse/filter/sort/bundle_suggest.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
