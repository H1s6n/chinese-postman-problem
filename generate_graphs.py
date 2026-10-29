"""New reproducible examples; not a reconstruction of the original dataset."""
import argparse
import json
import random


def generate(count=100, vertices=8, seed=42):
    if count < 1 or not 2 <= vertices <= 10:
        raise ValueError("Use count >= 1 and 2–10 vertices for this small-graph demo.")
    rng = random.Random(seed)
    for _ in range(count):
        graph = [[0] * vertices for _ in range(vertices)]
        # A spanning tree guarantees connectivity.
        for i in range(1, vertices):
            j = rng.randrange(i)
            graph[i][j] = graph[j][i] = rng.randint(1, 10)
        for i in range(vertices):
            for j in range(i + 1, vertices):
                if graph[i][j] == 0 and rng.random() < 0.35:
                    graph[i][j] = graph[j][i] = rng.randint(1, 10)
        yield graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--vertices", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    for graph in generate(args.count, args.vertices, args.seed):
        print(json.dumps(graph))
