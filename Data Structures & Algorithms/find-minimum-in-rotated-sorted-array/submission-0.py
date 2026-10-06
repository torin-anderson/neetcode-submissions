#We can use binary search. We just have to compare left to right to see whether we are in the rotated part or not. If left is higher than right then we want to change left to up from the middle
#Time O(logn)
#Space O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right:
            mid = left + (right - left) //2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]