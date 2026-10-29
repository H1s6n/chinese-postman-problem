"""Portfolio demonstration added after the original coursework."""
from coursework_solver import CPP

EXAMPLE = [
    [0, 8, 0, 6, 5],
    [8, 0, 6, 0, 5],
    [0, 6, 0, 8, 5],
    [6, 0, 8, 0, 5],
    [5, 5, 5, 5, 0],
]

if __name__ == "__main__":
    result = CPP(EXAMPLE)
    print(f"Minimum closed-route cost: {result} (expected: 60)")
    assert result == 60
