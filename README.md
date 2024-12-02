# Algorithms Tasks

## Grading and Policies
1. Students who use the Internet to plagiarize the task, or copy from their colleagues, will receive a grade of zero.
2. The task grade is **10**.

## Deliverables
1. Implementation of at least **two algorithms** without using built-in functions. Algorithms can be both recursive and non-recursive.
2. Documentation that includes:
   - Pseudo-code of the implemented algorithms.
   - Analysis of the algorithms used.
   - Computation of their time complexity.
   - Comparison between the algorithms.

## Task 1: Max Product of Three

### Problem Description
A non-empty zero-indexed array `A` consisting of `N` integers is given. The product of triplet 
`(P, Q, R)` equates to `A[P] * A[Q] * A[R]` (0 ≤ P < Q < R < N).

For example, array `A` such that:
product of triplet 
`(P, Q, R)` equates to `A[P] * A[Q] * A[R]` (0 ≤ P < Q < R < N).

For example, array `A` such that:
A[0] = -3 A[1] = 1 A[2] = 2 A[3] = -2 A[4] = 5 A[5] = 6

contains the following example triplets:

- (0, 1, 2), product is `-3 * 1 * 2 = -6`
- (1, 2, 4), product is `1 * 2 * 5 = 10`
- (2, 4, 5), product is `2 * 5 * 6 = 60`


Your goal is to find the maximal product of any triplet. Write a function that, given a non-empty zero-indexed array `A`, returns the value of the maximal product of any triplet.

## Example 1:
**Input:** `nums = [1, 2, 3]`  
**Output:** `6`

## Example 2:
**Input:** `nums = [1, 2, 3, 4]`  
**Output:** `24`

