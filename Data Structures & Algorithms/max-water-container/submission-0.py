#maximum area, returning this maximum area. Have to go off of lower side for height
#My thought is to have two pointers, and depending on which pointer in the heights array is lower change that one. We will iterate while left < right and each iteration we will check to see if the current area is higher than the previously highest array we found, which we will sotre in an array
#The time will be O(n) because we have to go through heights once
#The space will be O(1) because we are only storing a signle constant sized variable
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        maxA = (right - left) * min(heights[left], heights[right])

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            maxA = max(maxA,(right - left) * min(heights[left], heights[right]))
        
        
        return maxA
        