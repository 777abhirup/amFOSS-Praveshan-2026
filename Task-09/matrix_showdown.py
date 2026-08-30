import random
import time


def naive_multiply(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def split(m):
    n = len(m)
    mid = n // 2
    return ([row[:mid] for row in m[:mid]], [row[mid:] for row in m[:mid]],
            [row[:mid] for row in m[mid:]], [row[mid:] for row in m[mid:]])


def combine(c11, c12, c21, c22):
    top = [c11[i] + c12[i] for i in range(len(c11))]
    bottom = [c21[i] + c22[i] for i in range(len(c21))]
    return top + bottom


def next_power_of_two(n):
    return 1 if n <= 1 else 2 ** ((n - 1).bit_length())


def pad(m, size):
    return [row + [0] * (size - len(row)) for row in m] + [[0] * size for _ in range(size - len(m))]


def trim(m, rows, cols):
    return [row[:cols] for row in m[:rows]]


def divide_conquer_square(a, b):
    n = len(a)
    if n <= 32:
        return naive_multiply(a, b)
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    c11 = add(divide_conquer_square(a11, b11), divide_conquer_square(a12, b21))
    c12 = add(divide_conquer_square(a11, b12), divide_conquer_square(a12, b22))
    c21 = add(divide_conquer_square(a21, b11), divide_conquer_square(a22, b21))
    c22 = add(divide_conquer_square(a21, b12), divide_conquer_square(a22, b22))
    return combine(c11, c12, c21, c22)


def divide_conquer(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    size = next_power_of_two(max(rows, inner, cols))
    return trim(divide_conquer_square(pad(a, size), pad(b, size)), rows, cols)


def strassen_square(a, b):
    n = len(a)
    if n <= 32:
        return naive_multiply(a, b)
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    p1 = strassen_square(a11, sub(b12, b22))
    p2 = strassen_square(add(a11, a12), b22)
    p3 = strassen_square(add(a21, a22), b11)
    p4 = strassen_square(a22, sub(b21, b11))
    p5 = strassen_square(add(a11, a22), add(b11, b22))
    p6 = strassen_square(sub(a12, a22), add(b21, b22))
    p7 = strassen_square(sub(a11, a21), add(b11, b12))
    c11 = add(sub(add(p5, p4), p2), p6)
    c12 = add(p1, p2)
    c21 = add(p3, p4)
    c22 = sub(sub(add(p5, p1), p3), p7)
    return combine(c11, c12, c21, c22)


def strassen(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    size = next_power_of_two(max(rows, inner, cols))
    return trim(strassen_square(pad(a, size), pad(b, size)), rows, cols)


def benchmark(fn, a, b):
    start = time.perf_counter()
    result = fn(a, b)
    elapsed = (time.perf_counter() - start) * 1000
    return result, elapsed


def random_matrix(rows, cols, limit=9):
    return [[random.randint(0, limit) for _ in range(cols)] for _ in range(rows)]


def read_matrix(name, rows, cols):
    print(f"Enter {name} ({rows} rows, {cols} columns), one row at a time:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Please enter exactly {cols} integers.")
    return matrix


def main():
    print("=== Matrix Multiplication Showdown ===")
    mode = input("Use random matrices? (y/n): ").strip().lower()
    try:
        r1, inner, c2 = map(int, input("Enter dimensions r1 x inner x c2: ").split())
        if min(r1, inner, c2) <= 0:
            raise ValueError
    except ValueError:
        print("Invalid dimensions.")
        return

    if mode == "y":
        a = random_matrix(r1, inner)
        b = random_matrix(inner, c2)
        print("A =", a)
        print("B =", b)
    else:
        a = read_matrix("A", r1, inner)
        b = read_matrix("B", inner, c2)

    methods = [("Naive Matrix Multiplication", naive_multiply),
               ("Divide and Conquer", divide_conquer),
               ("Strassen's Algorithm", strassen)]
    results = []
    for name, fn in methods:
        result, elapsed = benchmark(fn, a, b)
        results.append((name, result, elapsed))

    reference = results[0][1]
    print("\nResults:")
    for name, result, elapsed in results:
        print(f"{name:<30} {elapsed:.3f} ms")
    print("Verification Status:", "PASSED" if all(r == reference for _, r, _ in results) else "FAILED")
    fastest = min(results, key=lambda item: item[2])
    print("Fastest Method:", fastest[0])
    print("\nResult matrix:")
    for row in reference:
        print(*row)


if __name__ == "__main__":
    main()
