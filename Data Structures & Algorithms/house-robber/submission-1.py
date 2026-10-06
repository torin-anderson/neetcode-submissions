class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        bestVal = [0] * len(nums)
        bestVal[0] = nums[0]
        bestVal[1] = max(nums[0], nums[1])        

        for num in range(2,len(nums)):
            bestVal[num] = max(bestVal[num-1], bestVal[num-2] + nums[num])
        return bestVal[-1]