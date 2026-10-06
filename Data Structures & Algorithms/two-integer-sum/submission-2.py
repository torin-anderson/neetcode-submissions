class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        diff = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[diff] = i
        return [-1,-2]