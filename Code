#Runtime 2ms
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        if len(nums) < 3:
            return 0
        
        for num in nums:
            if num < 0:
                if num < min2:
                    if num <= min1:
                        min2 = min1
                        min1 = num
                    else:
                        min2 = num
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

        if min1 <= 0 and min2 <= 0 and max1 >= 0 and min1 * min2 > max2*max3:
            return min1 * min2 * max1
        return max1 * max2 * max3
#Runtime 10ms
class Solution(object):
    def maximumProduct(self, nums):
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
    
        for num in nums:
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
        
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
    
        return max(max1 * max2 * max3, min1 * min2 * max1)
#Runtime 15ms
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3, min1, min2 = min(nums), min(nums), min(nums), 0, 0
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
                
        return max(max1*max2*max3,max1*min1*min2)
#Runtime 23ms
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
#Runtime 36ms
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        threeLowToHigh=nums[-1] * nums[-2] * nums[-3]
        threeHighToLow=nums[0] * nums[1] * nums[-1]
        maxOfThree=max(threeLowToHigh, threeHighToLow)
        
        return maxOfThree
