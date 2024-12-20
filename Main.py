def max_product_of_three(arr):
    # to make sure that the number is always bigger than the max or always smaller than the min
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    min1 = float('inf')
    min2 = float('inf')
    

    # checking wether the number is smaller than the two min variables or only one
    for num in arr:
        if num < 0: #To save computing time.
            if num < min2:
                if num <= min1: 
                    min2 = min1
                    min1 = num
                else:
                    min2 = num
        # checking wether the number is bigger than all 3 Max variables or only 2 of them or only one
        if num > max3:
            if num > max2:
                if num >= max1:
                    max3 = max2
                    max2 = max1
                    max1 = num
                else:
                    max3 = max2
                    max2 = num
            else:
                max3 = num
        

    if min2 < 0: # to make sure that the number is negative
        if max1 * max2 * max3 > min1 * min2 * max1:
            return max1 * max2 * max3
        else:
            return min1 * min2 * max1
    else: 
        return max1 * max2 * max3


arr = [1, 8, -5, 10, -17, 8, 8]

print(max_product_of_three(arr))

#recursive_code!!
def max_product_of_three_recursive(arr, index=0, max1=float('-inf'), max2=float('-inf'), max3=float('-inf'), min1=float('inf'), min2=float('inf')):
    # Base case: when we've processed all elements
    if index == len(arr):
        if min2 < 0:
            if max1 * max2 * max3 > min1 * min2 * max1:
                return max1 * max2 * max3
            else:
                return min1 * min2 * max1
        else:
            return max1 * max2 * max3
    
    num = arr[index]  # current number
    
    # Update min1 and min2 if necessary
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

    # Update max1, max2, max3 if necessary
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num
    
    # Recurse with the next index
    return max_product_of_three_recursive(arr, index + 1, max1, max2, max3, min1, min2)

# Test the recursive function
arr = [1, 8, 5, 10, 17, 8, 8]
print(max_product_of_three_recursive(arr))
