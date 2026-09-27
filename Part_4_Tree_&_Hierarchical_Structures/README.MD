# DSA Project Specs — Part 4: Trees & Hierarchical Structures

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

## 25. BST From Scratch (T1)

**Input:** `insert(value)`, `delete(value)`, `search(value)`; traversal requests (in/pre/post-order). **Output:** Correct traversal orderings; boolean from `search()`; a tree that remains a valid BST after every delete.

**Edge cases:**

- Deleting a node with 0, 1, or 2 children — the 2-children case (replace with in-order successor/predecessor) is where almost every BST bug lives
- Deleting the root node specifically
- Inserting a duplicate value — decide the policy (reject, insert as right child, or maintain a count) and be consistent
- `search()` on an empty tree
- Deleting a value that doesn't exist in the tree
- A degenerate tree (all left or all right children only, effectively a linked list) — your balance checker should correctly flag this

**Suggested structure:**

```
bst/
├── bst.py              # insert/delete/search
├── traversals.py       # in/pre/post-order
├── balance_checker.py  # height-based balance check
└── tests/
    └── test_bst.py     # all three delete cases, explicitly
```

---

## 26. File-System Explorer (T2)

**Input:** A root path (or a synthetic in-memory file tree); a `search(name)` query. **Output:** Matching file/folder paths.

**Edge cases:**

- Symbolic links that point back up the tree, creating a cycle — this breaks the "it's a tree" assumption; must detect and avoid infinite traversal
- Permission-denied folders encountered mid-traversal — skip and continue, don't crash the whole search
- Case-sensitive vs. case-insensitive search (platform-dependent — decide and document)
- Empty folders
- A search term matching both a file name and a folder name

**Suggested structure:**

```
fs-explorer/
├── tree_builder.py   # builds an in-memory tree from a real or synthetic FS
├── search.py         # name-based search over the tree
└── tests/
    └── test_search.py   # cycle detection specifically
```

---

## 27. Heap From Scratch (T1)

**Input:** `insert(value)`, `extract_min()` / `extract_max()`, `peek()`; optionally `heapify(array)`. **Output:** Correct min/max maintained after every operation; the internal array satisfies the heap property after every mutation.

**Edge cases:**

- `extract()` on an empty heap
- Heap with exactly one element
- Inserting duplicate values
- Sift-up/sift-down at the boundaries (root, last leaf) — index math here is the usual bug source
- Building a heap from an existing unsorted array should be implemented as `heapify` in O(n), not as n individual `insert()` calls (which would be O(n log n))

**Suggested structure:**

```
heap/
├── heap.py           # insert/extract/peek/heapify
└── tests/
    └── test_heap.py  # heap-property verification after every operation
```

---

## 28. Leaderboard / Compressor (T2)

Two directions for this slot — pick one:

### Direction A: Live Leaderboard

**Input:** A stream of `(user, score)` updates; `top_k()` queries at any time. **Output:** The current top K users by score.

**Edge cases:**

- A user's score updating multiple times — must update that user's position, not insert a duplicate entry
- Ties in score — needs a defined tie-breaking rule (e.g., earliest achieved first)
- `k` larger than the total number of users — return everyone, not an error

**Suggested structure:**

```
leaderboard/
├── leaderboard.py   # heap + hash map: O(log n) update, O(k) top-k read
└── tests/
    └── test_leaderboard.py
```

### Direction B: Huffman Compressor

**Input:** A text/byte stream to compress; the compressed output to later decompress. **Output:** Compressed bytes; a decompressed result that exactly matches the original.

**Edge cases:**

- Input with only one distinct character — a single-symbol Huffman tree can't produce a normal variable-length code; needs explicit special-case handling
- Empty input
- Round-trip correctness — decompressed output must be byte-for-byte identical to the original input, always test this explicitly

**Suggested structure:**

```
huffman-compressor/
├── huffman_tree.py
├── encoder.py
├── decoder.py
└── tests/
    └── test_roundtrip.py
```

---

## 29. Trie From Scratch (T1)

**Input:** `insert(word)`, `search(word)`, `starts_with(prefix)`, `delete(word)`. **Output:** Boolean from `search()`/`starts_with()`; correct trie structure after `delete()`.

**Edge cases:**

- Deleting a word that is itself a prefix of another stored word — must *not* remove the shared nodes the other word still needs
- Inserting the empty string
- Case sensitivity (decide and document)
- A prefix that exists as an internal path but was never inserted as a complete word — `starts_with()` should return true, `search()` should return false for it
- Deleting a word that was never inserted

**Suggested structure:**

```
trie/
├── trie.py           # insert/search/starts_with/delete
└── tests/
    └── test_trie.py  # shared-prefix deletion specifically
```

---

## 30. Autocomplete Engine (T2)

**Input:** A preloaded dictionary of words; a partial string as the user types. **Output:** A ranked list of suggested completions.

**Edge cases:**

- No matches for the given prefix — return an empty list cleanly, not an error
- A very short prefix (single letter) matching thousands of words — cap the number of suggestions returned, and rank by something meaningful (frequency/popularity), since raw trie traversal order isn't inherently useful
- Case mismatch between user input and stored dictionary casing
- Updating suggestion ranking as words get "used" more over time (optional enhancement, not required for a working version)

**Suggested structure:**

```
autocomplete/
├── trie.py         # reuses/extends the trie from Project 29
├── ranker.py       # frequency-based suggestion ranking
├── api.py          # query(prefix) -> ranked suggestions
└── tests/
    └── test_autocomplete.py
```

---
