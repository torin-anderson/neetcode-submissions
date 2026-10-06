#Returning 2 indices that add up to target. Indices can not be the same.
#We always have a solution available.
#Smallest index should be returned first.
#Way of thinking about this could be through multiple iterators. However, that would be a poor timing and could give us O(n^2) complexity.
#A more optimal solution should involve O(n) timing. We could look at using a hashmap where while we go through nums we have each key be the complementary value and each value be the index of the current value. WHile ietrating through nums we can see if the value is in the hashmap, thus finding if a complementary value exists, and when we do we return list of both the current index and the value within the hashmap.
#This will be O(n) because at most we will have to pass through nums entirely.
#This will be O(n) space too because at most we will have to add every value into the hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[target - nums[i]] = i
        return [-1,-1]