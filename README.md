# Chinese Postman Problem — KAU Coursework

Python coursework for **CS-611: Design & Analysis of Algorithms**, King Abdulaziz University, Faculty of Computing & Information Technology.

**Project team:** Fahad Farooq Jamie and Hassan Alharbi.  
**Supervisor:** Dr. Khalid Thabit.

The original presentation lists Hassan under his earlier name, Hassan M Aloufi. This portfolio uses his current preferred name. Individual coding responsibilities have not been established from the supplied files.

## Purpose

Find the minimum cost of a **closed walk covering every edge at least once** in a connected, undirected, weighted graph. The implementation returns the cost, not the actual route.

The coursework identifies odd-degree vertices, enumerates their pairings, computes shortest-path costs with a custom Dijkstra implementation, and adds the cheapest pairing cost to the original edge total. The pairing search grows rapidly with the number of odd-degree vertices, so this implementation is intended for small educational examples.

## Quick start

Python 3; no third-party packages required. Run from this repository's root:

```bash
python demo.py
python -m unittest -v test_examples
```

Expected demo output:

```text
Minimum closed-route cost: 60 (expected: 60)
```

On systems where Python is named `python3`, use that command instead.

## Files

| File | Purpose |
|---|---|
| `original/code_chinesepp.py` | Original coursework script, unchanged |
| `original/1run.bat` | Original Windows launcher, unchanged |
| `coursework_solver.py` | Original functions extracted without algorithm changes; no dataset import or benchmark execution |
| `demo.py` | Later portfolio addition using the presentation's example |
| `generate_graphs.py` | Later addition generating small connected undirected graphs |
| `test_examples.py` | Known-cost checks and generator checks |

## Worked example

Vertices A–E correspond to matrix indices 0–4 in `demo.py`.

- Original edge total: **48**.
- Odd-degree vertices: **A, B, C, D**.
- Pairing costs: AB/CD = 16; AD/BC = 12; AC/BD = 20.
- Minimum added cost: **12**, obtained by duplicating AD and BC.
- Optimal closed-route cost: **48 + 12 = 60**.

The original slides incorrectly derive 48 by summing the three candidate pairing costs. Their sum happens to equal the graph's edge total in this example, but that is not the general method. Also, an Eulerian circuit covers each **edge** exactly once; it does not require visiting each vertex only once.

## Original dataset and limitations

The supplied dataset contains batches of 1,000, 10,000, 100,000 and 1,000,000 small matrices. These labels refer to graph counts, not numbers of vertices per graph. The original file is approximately 230.5 MB and is omitted from this lightweight repository.

A review sampled the first 100 graphs in each batch. All 400 sampled matrices were asymmetric and had nonzero diagonal entries. These inputs do not match this solver's undirected, loop-free graph assumptions. Its degree counting also does not correctly account for self-loops. Consequently, original timings should not be treated as validation of correct Chinese Postman solutions. No new benchmark results are claimed here.

Other limitations of the original solver include finite hard-coded infinity values, no input validation, and possible failure or nontermination on disconnected or sufficiently high-weight inputs. Use the small positive-integer examples supplied here. The tests cover four known-cost cases, not all possible graphs.

The original Windows launcher expects `dataset.py` beside the original script. It is preserved for historical reference, not the recommended quick-start command. The supplied compiled executable is not included or verified.

## Generate new examples

```bash
python generate_graphs.py --count 100 --vertices 8 --seed 42 > generated_graphs.jsonl
```

This creates JSON Lines data, one adjacency matrix per line. It is a **new dataset**, not the original benchmark dataset and not a drop-in `dataset.py`. Matrices are symmetric, have zero diagonals, and contain a spanning tree to ensure connectivity. Graph size is deliberately limited to 2–10 vertices.

## Portfolio scope and attribution

This repository preserves coursework and separates later maintenance additions from the original submission. It demonstrates graph representation, shortest paths, recursive pairing and the importance of validating benchmark inputs. It does not claim a novel algorithm.

The PDF and presentation are not bundled: their explanations need correction and they contain student identifiers. No blanket open-source licence has been assigned to the joint coursework; agree licensing with all contributors before adding one. Credit any external source used in the original implementation if identified.
