# DSA: Build Your Way to Mastery

67 hands-on projects that turn each data structure and algorithm into something you build, test, and measure. Every project comes with boilerplate already in place: folder layout, function signatures, one test stub per edge case, and config. The logic, the tie-breaks, and the assertions are yours to write.

## Docs

| File | What it covers |
| --- | --- |
| [DSA Fundamentals](<DSA Fundamentals.md>) | The concepts themselves |
| [DSA Project Roadmap](<DSA Project Roadmap.md>) | The three project types (T1 isolated, T2 applied, T3 capstone) and the suggested build order |
| [Project Briefs](<DSA Project Briefs - Problem Statements & Objectives.md>) | Problem statement and objective for every project |
| `Part_*/README.MD` | Full spec per project: input/output, edge cases, suggested structure |

## Layout

| Folder | Projects | Shared helpers (`_shared/`) |
| --- | --- | --- |
| [Part_1_Foundations](Part_1_Foundations) | 01–08 | `bench_harness.py`: timing decorator, median-of-trials `measure()`, CSV writer |
| [Part_2_Linear_Structures](Part_2_Linear_Structures) | 09–14 | none |
| [Part_3_Core_Algo_Patterns](Part_3_Core_Algo_Patterns) | 15–24 | none |
| [Part_4_Tree_&_Hierarchical_Structures](<Part_4_Tree_&_Hierarchical_Structures>) | 25–30 | `tree_debug.py`: print any tree or heap array (cycle-safe) |
| [Part_5_Graphs](Part_5_Graphs) | 31–40 | `random_graphs.py`: random, DAG, connected, and grid generators |
| [Part_6_Dynamic_Programming](Part_6_Dynamic_Programming) | 41–47 | `random_cases.py`: small random inputs for cross-checking DP answers |
| [Part_7_Greedy_Algos](Part_7_Greedy_Algos) | 48–49 | none |
| [Part_8_Advanced_Topics](Part_8_Advanced_Topics) | 50–57 | `bits.py`: masks and binary display; `fixtures.py`: save/replay range-query fixtures |
| [Part_9_Capstone_Projects](Part_9_Capstone_Projects) | 01–10 | none (each capstone has its own `models.py`) |
| [scaffold](scaffold) | | The generator that creates all of the above |

Each project folder (`NN_<name>/`) contains:

```
NN_<name>/
├── README.md          # problem, objective, full spec, scaffold notes, run instructions
├── <modules>.py       # signatures + docstrings; bodies raise NotImplementedError
├── tests/test_*.py    # one stub per edge-case bullet, TODO = the bullet text
├── requirements.txt   # pytest
├── pytest.ini         # puts the project (and ../_shared) on the import path
└── .gitignore
```

Slots with two directions (14, 28, 36, 47, 51) contain `A_<name>/` and `B_<name>/` subfolders, each a self-contained project. Pick one and delete the other. Project 02 (Big-O Visualizer) is plain JavaScript with no dependencies.

## Working on a project

```bash
cd Part_1_Foundations/07_hash-table
pip install -r requirements.txt   # once; any Python 3.10+
pytest
```

Then:

1. Read the project's `README.md`.
2. Replace each `raise NotImplementedError` with your implementation.
3. Fill in the assertions under each `# TODO` in `tests/`.

The stub tests pass as generated because their bodies are just `...`. A green run means nothing until you've written the assertions.

To run a script that imports a shared helper outside pytest, put `_shared` on the path:

```bash
PYTHONPATH=../_shared python bench.py
```

For the JavaScript project:

```bash
cd Part_1_Foundations/02_bigo-visualizer
npm test                 # node --test
python3 -m http.server   # open http://localhost:8000 (module workers need http://, not file://)
```

## Scaffold: regenerating boilerplate

`scaffold/gen.py` rebuilds boilerplate from the specs. **It is safe by default: existing files are never touched and only missing ones are created**, so you can rerun it any time to restore something you deleted.

```bash
python3 scaffold/gen.py                               # restore missing files, all parts
python3 scaffold/gen.py p5 cap                        # only Part 5 and the capstones
python3 scaffold/gen.py --only hash-table             # only folders whose name contains "hash-table"
python3 scaffold/gen.py --only B_huffman              # bring back a deleted direction folder
python3 scaffold/gen.py --only 07_hash-table --force --dry-run   # preview resetting one project to stubs
python3 scaffold/gen.py --only 07_hash-table --force             # actually reset it (your code is replaced)
python3 scaffold/gen.py --help
```

| Option | Effect |
| --- | --- |
| `PART ...` | Limit to parts: `p1` … `p8`, `cap` (default: all) |
| `--only NAME ...` | Limit to project folders, direction folders, or `_shared` whose name contains `NAME`. Substring match, so `07` hits both `07_hash-table` and capstone `07_social-network-analyzer`; use the full folder name or add a `PART`. |
| `--force` | Overwrite existing files that differ from the generated version. **This replaces your code with stubs.** |
| `--dry-run` | Print what would be created or overwritten without writing anything |

Behavior worth knowing:

- **Deleted direction folders stay deleted.** If you keep `A_…` and delete `B_…`, a normal run won't recreate `B_…`. Name it with `--only` to bring it back; that touches only the named direction.
- **Any missing file is recreated,** including optional ones like `plot.py`. Scope the run with `PART` or `--only` if you've pruned files on purpose.
- **Spec docs are read live.** Problem statements, objectives, and edge-case bullets come from the Briefs doc and `Part_*/README.MD`. Editing those and running with `--force --only <project>` refreshes that project's `README.md` and test TODOs. Test stub names must still line up one-to-one with the edge-case bullets, or the generator stops with an assertion.
- **Renaming a Part folder:** update the `PARTS` table at the top of `scaffold/gen.py`.

### Where things live in `scaffold/`

| File | Contents |
| --- | --- |
| `gen.py` | The generator: parses the docs, writes READMEs, stubs, tests, and config |
| `p1.py` … `p8.py`, `cap.py` | Per-part specs: module stub sources, test stub names, shared helpers (`SHARED`), scaffold notes |
| `dsl.py` | `P` / `D` / `DIRS` project builders, plus the reused `Graph`, `UnionFind`, and `FenwickTree` snippets |

To change what a project's stubs look like, edit its entry in the matching `p*.py`, then regenerate that project with `--force --only <name>`, previewing with `--dry-run` first.
