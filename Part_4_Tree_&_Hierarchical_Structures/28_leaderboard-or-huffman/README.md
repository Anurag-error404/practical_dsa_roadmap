# Leaderboard / Compressor (T2)

*Part 4 — Trees & Hierarchical Structures*

## Problem

"Top 10 right now" shouldn't require re-sorting the entire dataset on every update.

## Objective

Build a top-K service using a heap, or a file compressor using your own Huffman coding.

---

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

## Run

Run inside the direction folder you keep:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../../_shared python <script>.py`.

This slot has two directions (`A_leaderboard/`, `B_huffman-compressor/`). Pick one and delete the other.
