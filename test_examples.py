"""Small regression tests; not proof of correctness for arbitrary inputs."""
import unittest
from coursework_solver import CPP
from demo import EXAMPLE
from generate_graphs import generate

class Examples(unittest.TestCase):
    def test_known_costs(self):
        cases = [(EXAMPLE, 60), ([[0,2,4],[2,0,3],[4,3,0]],9),
                 ([[0,2,0],[2,0,3],[0,3,0]],10),
                 ([[0,1,2,3],[1,0,0,0],[2,0,0,0],[3,0,0,0]],12)]
        for graph, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(CPP(graph), expected)

    def test_generator_contract(self):
        for n in range(2,11):
            for g in generate(10,n):
                self.assertTrue(all(g[i][i] == 0 for i in range(n)))
                self.assertTrue(all(g[i][j] == g[j][i] >= 0 for i in range(n) for j in range(n)))
                seen = {0}
                stack = [0]
                while stack:
                    i = stack.pop()
                    for j,w in enumerate(g[i]):
                        if w and j not in seen:
                            seen.add(j)
                            stack.append(j)
                self.assertEqual(len(seen),n)
        self.assertEqual(list(generate()),list(generate()))

if __name__ == "__main__":
    unittest.main()
