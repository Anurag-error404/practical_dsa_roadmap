"""Scaffold generator for the DSA roadmap: README, stubs, test stubs, config for every project.

Specs live next to this file (p1.py .. p8.py, cap.py); problem/objective/edge-case text is read from the
roadmap docs. Safe by default: existing files are never touched, only missing ones are created.

    python3 scaffold/gen.py                      # restore any missing boilerplate, all parts
    python3 scaffold/gen.py p5 cap               # only Part 5 and the capstones
    python3 scaffold/gen.py --only hash-table    # only projects whose folder name contains "hash-table"
    python3 scaffold/gen.py --only 07_hash-table --force --dry-run   # preview resetting one project to stubs
"""
import argparse
import ast
import importlib
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))

PARTS = {
    "p1": ("Part_1_Foundations", "Part 1 — Foundations", 8),
    "p2": ("Part_2_Linear_Structures", "Part 2 — Linear Structures", 6),
    "p3": ("Part_3_Core_Algo_Patterns", "Part 3 — Core Algorithmic Patterns", 10),
    "p4": ("Part_4_Tree_&_Hierarchical_Structures", "Part 4 — Trees & Hierarchical Structures", 6),
    "p5": ("Part_5_Graphs", "Part 5 — Graphs", 10),
    "p6": ("Part_6_Dynamic_Programming", "Part 6 — Dynamic Programming", 7),
    "p7": ("Part_7_Greedy_Algos", "Part 7 — Greedy Algorithms", 2),
    "p8": ("Part_8_Advanced_Topics", "Part 8 — Advanced Topics", 8),
    "cap": ("Part_9_Capstone_Projects", "Type 3 — Capstones", 10),
}
BRIEF_HEADERS = {f"## Part {i}": f"p{i}" for i in range(1, 9)} | {"## Type 3": "cap"}
HEAD = re.compile(r"^## (?:(\d+)\. |Capstone (\d+): )(.+)$", re.M)

GITIGNORE_PY = "__pycache__/\n*.py[cod]\n.pytest_cache/\n.venv/\n"
GITIGNORE_JS = "node_modules/\n.DS_Store\n"


def src(text: str) -> str:
    return textwrap.dedent(text).strip("\n") + "\n"


OPTS = argparse.Namespace(force=False, dry_run=False, only=[])
STATS = {"created": 0, "overwritten": 0, "kept": 0}


def selected(name: str) -> bool:
    return not OPTS.only or any(o in name for o in OPTS.only)


def write(path: Path, text: str) -> None:
    """Create missing files; overwrite existing ones only with --force (and only if they differ)."""
    if path.exists():
        if not OPTS.force or path.read_text() == text:
            STATS["kept"] += 1
            return
        status = "overwritten"
    else:
        status = "created"
    STATS[status] += 1
    print(f"{'would be ' if OPTS.dry_run else ''}{status}: {path.relative_to(ROOT)}")
    if not OPTS.dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def parse_briefs() -> dict:
    groups, cur = {}, None
    text = (ROOT / "DSA Project Briefs - Problem Statements & Objectives.md").read_text()
    for line in text.splitlines():
        for prefix, key in BRIEF_HEADERS.items():
            if line.startswith(prefix):
                cur = key
        if cur and line.startswith("|") and not line.startswith(("| ---", "| Project", "| Capstone")):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            groups.setdefault(cur, []).append(cells)
    return groups


def parse_spec(path: Path) -> list:
    text = path.read_text()
    ms = list(HEAD.finditer(text))
    out = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        body = re.sub(r"\n---\s*$", "", text[m.end():end].strip()).strip()
        out.append((int(m[1] or m[2]), m[3].strip(), body))
    return out


def edge_blocks(body: str) -> list:
    blocks, cur = [], None
    for line in body.splitlines():
        if line.startswith("**Edge cases"):
            cur = []
            blocks.append(cur)
        elif cur is not None:
            if line.startswith("- "):
                cur.append(re.sub(r"\*\*?([^*]+?)\*\*?", r"\1", line[2:].strip()))
            elif line.strip() and cur:
                cur = None
    return blocks


def public_names(code: str) -> list:
    tree = ast.parse(code)
    return [
        n.name for n in tree.body
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and not n.name.startswith("_") and n.name != "main"
    ]


def todo(bullet: str, indent: str, comment: str) -> str:
    lines = textwrap.wrap(bullet, 84)
    first = f"{indent}{comment} TODO: {lines[0]}"
    rest = [f"{indent}{comment}       {ln}" for ln in lines[1:]]
    return "\n".join([first, *rest])


def py_test_file(files: dict, bullets: list, names: list, extra_imports: list) -> str:
    modules = {}
    for rel, code in files.items():
        if rel.endswith(".py") and not rel.startswith("tests/"):
            names_ = public_names(code)
            if names_:
                modules[rel[:-3].replace("/", ".")] = names_
    all_names = [n for ns in modules.values() for n in ns]
    if len(all_names) != len(set(all_names)):
        imports = [f"import {m}" for m in modules]
    else:
        imports = [f"from {m} import {', '.join(ns)}" for m, ns in modules.items()]
    head = "\n".join(["import pytest", "", *imports, *extra_imports])
    tests = [f"def {name}():\n{todo(b, '    ', '#')}\n    ..." for name, b in zip(names, bullets)]
    return head + "\n\n\n" + "\n\n\n".join(tests) + "\n"


def js_test_file(bullets: list, names: list, extra_imports: list) -> str:
    head = "\n".join(['import { test } from "node:test";', 'import assert from "node:assert/strict";', "", *extra_imports])
    tests = [f'test("{name}", () => {{\n{todo(b, "  ", "//")}\n}});' for name, b in zip(names, bullets)]
    return head + "\n\n" + "\n\n".join(tests) + "\n"


def readme(title, part_label, brief, body, project, has_shared) -> str:
    _, problem, objective = brief
    run = []
    if project.js:
        run += ["```bash", "npm test                    # node --test, no dependencies", "python3 -m http.server     # then open http://localhost:8000 (module workers need http://, not file://)", "```"]
    else:
        where = "inside the direction folder you keep" if project.subs[0].dir else "from this folder"
        run += [f"Run {where}:", "", "```bash", "pip install -r requirements.txt", "pytest", "```"]
        if has_shared:
            shared = "../../_shared" if project.subs[0].dir else "../_shared"
            run += ["", f"Shared helpers in `{shared}/` are already on the pytest path. For scripts: `PYTHONPATH={shared} python <script>.py`."]
    if project.subs[0].dir:
        dirs = ", ".join(f"`{s.dir}/`" for s in project.subs)
        run += ["", f"This slot has two directions ({dirs}). Pick one and delete the other."]
    parts = [
        f"# {title}", "", f"*{part_label}*", "",
        "## Problem", "", problem, "",
        "## Objective", "", objective, "",
        "---", "", body, "",
    ]
    if project.notes:
        parts += ["---", "", "## Scaffold notes", "", *[f"- {n}" for n in project.notes], ""]
    parts += ["---", "", "## Run", "", *run, ""]
    return "\n".join(parts)


def build_part(key: str, spec_mod) -> int:
    part_dir, part_label, expected = PARTS[key]
    base = ROOT / part_dir
    specs = parse_spec(base / "README.MD")
    briefs = parse_briefs()[key]
    assert len(specs) == len(briefs) == expected == len(spec_mod.PROJECTS), (key, len(specs), len(briefs), len(spec_mod.PROJECTS))
    shared = getattr(spec_mod, "SHARED", {})
    if selected("_shared"):
        for name, code in shared.items():
            write(base / "_shared" / name, src(code))

    built = 0
    for (n, title, body), brief, project in zip(specs, briefs, spec_mod.PROJECTS):
        assert n == project.n, (key, n, project.n)
        pdir = base / f"{n:02d}_{project.dir}"
        whole = selected(pdir.name)
        named = [s for s in project.subs if s.dir and OPTS.only and selected(s.dir)]
        if not (whole or named):
            continue
        built += 1
        blocks = edge_blocks(body)
        if whole:
            write(pdir / "README.md", readme(title, part_label, brief, body, project, bool(shared)))
            if project.js:
                write(pdir / ".gitignore", GITIGNORE_JS)
            else:
                write(pdir / "requirements.txt", "\n".join(["pytest>=7.0", *project.requirements]) + "\n")
                write(pdir / ".gitignore", GITIGNORE_PY)
        picked = [s for s in project.subs if s.dir and (pdir / s.dir).exists()]
        for sub in project.subs:
            if named and sub not in named:
                continue
            # A deleted direction means you picked the other one; it comes back only when named via --only.
            if picked and sub not in picked and sub not in named:
                continue
            sdir = pdir / sub.dir if sub.dir else pdir
            files = {rel: src(code) for rel, code in sub.files.items()}
            for rel, code in files.items():
                write(sdir / rel, code)
            bullets = blocks[sub.edge]
            if sub.pick is not None:
                bullets = [bullets[i] for i in sub.pick]
            assert len(bullets) == len(sub.tests), (n, sub.dir, len(bullets), len(sub.tests), bullets)
            if project.js:
                write(sdir / sub.test_file, js_test_file(bullets, sub.tests, sub.extra_imports))
                continue
            pypath = " ".join([".", "../../_shared" if sub.dir else "../_shared"] if shared else ["."])
            write(sdir / "pytest.ini", f"[pytest]\ntestpaths = tests\npythonpath = {pypath}\n")
            write(sdir / sub.test_file, py_test_file(files, bullets, sub.tests, sub.extra_imports))
    return built


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Regenerate DSA project boilerplate (missing files only by default).")
    ap.add_argument("parts", nargs="*", metavar="PART", help=f"any of {', '.join(PARTS)} (default: all)")
    ap.add_argument("--only", nargs="+", default=[], metavar="NAME",
                    help="limit to project folders (or _shared / a direction folder) whose name contains NAME")
    ap.add_argument("--force", action="store_true", help="overwrite existing files that differ (replaces your code with stubs)")
    ap.add_argument("--dry-run", action="store_true", help="print what would change without writing")
    OPTS = ap.parse_args()
    if unknown := set(OPTS.parts) - set(PARTS):
        ap.error(f"unknown part(s): {', '.join(sorted(unknown))}")
    total = sum(build_part(k, importlib.import_module(k)) for k in OPTS.parts or PARTS)
    print(f"{total} projects: {STATS['created']} created, {STATS['overwritten']} overwritten, "
          f"{STATS['kept']} left untouched{' (dry run)' if OPTS.dry_run else ''}")
