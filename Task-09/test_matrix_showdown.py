from matrix_showdown import naive_multiply, divide_conquer, strassen
import random


def test_random_matrices():
    for rows, inner, cols in [(1, 1, 1), (2, 3, 4), (3, 5, 2), (8, 7, 6), (33, 33, 33)]:
        for _ in range(3):
            a = [[random.randint(-5, 5) for _ in range(inner)] for _ in range(rows)]
            b = [[random.randint(-5, 5) for _ in range(cols)] for _ in range(inner)]
            expected = naive_multiply(a, b)
            assert divide_conquer(a, b) == expected
            assert strassen(a, b) == expected
    print("All matrix multiplication tests passed.")


if __name__ == "__main__":
    test_random_matrices()
