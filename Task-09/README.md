# Task 09 — Matrix Multiplication Showdown

## Objective
Implement matrix multiplication using three approaches and compare their execution times.

## Implemented methods
1. **Naive multiplication** — standard triple-loop multiplication, O(n³).
2. **Divide and Conquer** — recursively splits matrices into four blocks; O(n³) asymptotically, with recursive structure.
3. **Strassen's algorithm** — reduces the number of recursive multiplications and has O(n^log₂7) ≈ O(n^2.807) complexity.

## Features
- Accepts user-entered matrix dimensions and elements.
- Optional random matrix generation.
- Measures execution time using Python's high-resolution timer.
- Verifies that all three algorithms produce the same result.
- Reports the fastest method.
- Supports rectangular matrices by padding internally for recursive methods.

## Run
```bash
python3 matrix_showdown.py
```

For random matrices, answer `y` when prompted. Otherwise answer `n` and enter the matrices row by row.

## Learning
This task helped me understand recursive divide-and-conquer algorithms, Strassen multiplication, matrix padding, benchmarking with `time.perf_counter()`, and result verification.

## Challenges
The main challenge was adapting recursive square-matrix algorithms to arbitrary matrix dimensions. I solved this by padding matrices to the next power-of-two square size and trimming the result afterward.
