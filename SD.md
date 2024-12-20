# MAX PRODUCT OF THREE

## Recursive Algorithm: MaxProductOfThreeRecursive

```python
MaxProductOfThreeRecursive(arr, index, max1, max2, max3, min1, min2):
1. If index == length(arr):
   2. If min2 < 0:
       3. If max1 * max2 * max3 > min1 * min2 * max1: 
           4. Return max1 * max2 * max3
       5. Else:
           6. Return min1 * min2 * max1
   7. Else:
       8. Return max1 * max2 * max3

9. num ← arr[index]

10. If num < min1:
    11. Update min2 ← min1
    12. Update min1 ← num
13. Else If num < min2:
    14. Update min2 ← num

15. If num > max1:
    16. Update max3 ← max2
    17. Update max2 ← max1
    18. Update max1 ← num
19. Else If num > max2:
    20. Update max3 ← max2
    21. Update max2 ← num
22. Else If num > max3:
    23. Update max3 ← num

24. Return MaxProductOfThreeRecursive(arr, index + 1, max1, max2, max3, min1, min2)

