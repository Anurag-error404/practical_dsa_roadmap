# Permissions System / Bloom Filter (T2)

*Part 8 — Advanced Topics*

## Problem

Checking "have I seen this before" across millions of items shouldn't need to store them all.

## Objective

Build a Unix-style flags/permissions system, or a Bloom filter for approximate membership testing.

---

Two directions for this slot — pick one:

### Direction A: Permissions System

**Input:** Defined permission flags (read/write/execute, etc.); assign flags to users via bitmask; `check(user, permission)`. **Output:** Boolean permission check result.

**Edge cases:**

- Checking a permission flag that was never defined — should error, not silently return false
- Combining/removing permissions (OR to add, AND-NOT to remove) — a common source of subtle bugs if the bit logic is inverted
- A user with zero permissions vs. a user with all permissions

### Direction B: Bloom Filter

**Input:** `add(item)`, `might_contain(item)`; configured filter size + number of hash functions. **Output:** Boolean — "definitely not present" or "possibly present."

**Edge cases:**

- False positives are expected and must be *tested for*, not treated as a bug
- False negatives must **never** occur — an item that was explicitly added must always return "might contain" true
- Filter size/hash-count chosen too small for the expected item count — leads to unacceptably high false-positive rates; document the size/accuracy trade-off

**Suggested structure:**

```
permissions-or-bloomfilter/
# Permissions variant:
├── permission_flags.py
├── user_permissions.py
└── tests/
    └── test_permissions.py

# Bloom filter variant:
├── bloom_filter.py   # bit array + multiple hash functions
└── tests/
    └── test_bloom_filter.py   # false-positive rate + false-negative guarantee
```

---

## Run

Run inside the direction folder you keep:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../../_shared python <script>.py`.

This slot has two directions (`A_permissions/`, `B_bloom-filter/`). Pick one and delete the other.
