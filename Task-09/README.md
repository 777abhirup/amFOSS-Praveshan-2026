# Task 09 - Matrix Multiplication Showdown

## About

This program compares three different ways of multiplying matrices:

* Naive Matrix Multiplication
* Divide and Conquer
* Strassen's Algorithm

The program takes the matrix dimensions and values from the user. It then runs all three methods, measures their execution time, and checks whether they produce the same result.

Random matrices can also be generated instead of entering the values manually.

## Algorithms

### 1. Naive Matrix Multiplication

This is the normal method of multiplying two matrices.

For every element in the result matrix, the program multiplies the corresponding row of the first matrix with the column of the second matrix.

The time complexity is:

```text
O(n³)
```

### 2. Divide and Conquer

The matrices are divided into four smaller parts.

The smaller matrices are multiplied recursively and the four resulting parts are combined to form the final matrix.

The asymptotic time complexity is still:

```text
O(n³)
```

In this program, smaller matrices are handled using the Naive method instead of continuing the recursion.

### 3. Strassen's Algorithm

Strassen's algorithm also divides the matrices into smaller parts, but it uses **7 recursive multiplications instead of 8**.

This reduces the number of multiplications needed for larger matrices.

Its time complexity is approximately:

```text
O(n^2.807)
```

## How It Works

The program first gets the matrix dimensions.

For example:

```text
A = 2 × 3
B = 3 × 2
```

The matrices are then passed to all three algorithms.

For each algorithm, the program:

1. Multiplies the matrices.
2. Measures the execution time.
3. Stores the result.
4. Compares the result with the Naive multiplication result.

The program finally displays the execution time of all three methods and the verification status.

## Benchmarking

Execution time is measured using Python's `time.perf_counter()`.

The time is measured immediately before and after each multiplication and converted to milliseconds.

Example:

```text
Naive Matrix Multiplication       0.123 ms
Divide and Conquer                0.156 ms
Strassen's Algorithm              0.142 ms

Verification Status: PASSED
```

The fastest method shown by the program is simply the method that took the least time for that particular run.

## Matrix Size Handling

Divide and Conquer and Strassen's algorithm work with square matrices whose size is convenient for recursive splitting.

To support rectangular matrices, the program pads them with zeros up to the next power-of-two square size.

After multiplication, the extra rows and columns are removed to get the required result size.

## Testing

A separate `test_matrix_showdown.py` file is included to test the three implementations.

It generates random matrices with different dimensions and checks that the Divide and Conquer and Strassen results match the Naive result.

Run the tests using:

```bash
python3 test_matrix_showdown.py
```

If everything works correctly:

```text
All matrix multiplication tests passed.
```

## Running the Program

Run the main program with:

```bash
python3 matrix_showdown.py
```

The program will ask whether random matrices should be used.

Enter:

```text
y
```

for random matrices, or:

```text
n
```

to enter the matrix values manually.

## Challenges

The main challenge was implementing the recursive algorithms while also supporting matrices that are not square.

Padding the matrices to a suitable square size and trimming the final result solved this problem.

Another challenge was making sure that all three algorithms produced exactly the same result.

## What I Learned

Through this task, I learned about:

* Matrix multiplication
* Recursion
* Divide and conquer
* Strassen's algorithm
* Time complexity
* Benchmarking with `time.perf_counter()`
* Matrix padding
* Writing simple automated tests in Python
