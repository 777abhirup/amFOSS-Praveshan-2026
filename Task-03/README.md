# Task 03: LeetCode Challenge

I solved 5 LeetCode problems using Python.

The problems include 3 Easy problems and 2 Medium problems.

## Problems Solved

| No. | Problem | Difficulty |
|---|---|---|
| 1 | Length of Last Word | Easy |
| 2 | Palindrome Number | Easy |
| 3 | Roman to Integer | Easy |
| 4 | Divide Two Integers | Medium |
| 5 | Jump Game | Medium |

---

## 1. Length of Last Word

**LeetCode Problem:** 58  
**Difficulty:** Easy

### Approach

I used the `split()` function to separate the sentence into words.

Then I selected the last word using `[-1]` and used `len()` to find its length.

### Example

```text
Input: "Hello World"
Output: 5
```

### Concepts Learned

- Strings
- `split()`
- Lists
- Negative indexing
- `len()`

### File

`length_of_last_word.py`

---

## 2. Palindrome Number

**LeetCode Problem:** 9  
**Difficulty:** Easy

### Approach

I first checked if the number was negative.

Then I converted the number into a string and reversed it using `[::-1]`.

Finally, I compared the original string with the reversed string.

If both are the same, the number is a palindrome.

### Example

```text
Input: 121
Output: True
```

```text
Input: 123
Output: False
```

### Concepts Learned

- `if` statements
- Strings
- String slicing
- Boolean values
- `str()`

### File

`palindrome_number.py`

---

## 3. Roman to Integer

**LeetCode Problem:** 13  
**Difficulty:** Easy

### Approach

I created a dictionary to store the value of each Roman numeral.

For example:

```text
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
```

I then checked each character.

If a smaller value comes before a larger value, I subtract it.

Otherwise, I add it.

### Example

```text
Input: "III"
Output: 3
```

```text
Input: "MCMXCIV"
Output: 1994
```

### Concepts Learned

- Dictionaries
- Loops
- Conditions
- Indexing
- Adding and subtracting values

### File

`roman_to_integer.py`

---

## 4. Divide Two Integers

**LeetCode Problem:** 29  
**Difficulty:** Medium

### Approach

The problem asks us to divide two integers and return the integer result.

I used Python's division and converted the result to an integer.

### Example

```text
Input: dividend = 10, divisor = 3
Output: 3
```

### Concepts Learned

- Functions
- Integer conversion
- Division
- Function parameters
- Return values

### File

`divide_two_integers.py`

> Note: The original LeetCode problem specifically asks to solve this without using multiplication, division, or modulo operators. I need to improve this solution later to fully follow that requirement.

---

## 5. Jump Game

**LeetCode Problem:** 55  
**Difficulty:** Medium

### Approach

I used a variable called `farthest` to keep track of the farthest position I can reach.

For every position, I check whether that position can be reached.

Then I update the farthest position using:

```python
i + nums[i]
```

If I reach a position that is beyond `farthest`, I return `False`.

If I can reach the end of the list, I return `True`.

### Example

```text
Input: [2,3,1,1,4]
Output: True
```

Here, the last index can be reached.

### Concepts Learned

- Lists
- Loops
- `if` conditions
- `max()`
- Greedy approach
- Tracking the maximum reachable position

### File

`jump_game.py`

---

## What I Learned

While solving these problems, I learned:

- Basic Python functions
- Strings and string operations
- Lists and indexing
- Dictionaries
- Loops
- Conditional statements
- Boolean values
- The `max()` function
- Basic problem-solving techniques
- Greedy thinking

These problems helped me understand how to break a programming problem into smaller steps and implement the solution in Python.

## Conclusion

This task helped me practice Python and improve my basic problem-solving skills through LeetCode problems.