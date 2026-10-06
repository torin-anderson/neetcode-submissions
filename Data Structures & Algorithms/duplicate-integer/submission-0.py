#See if there are any duplicate values in the array
#Return true if duplicates
#Looking towards hashing, specifically a hashset because that will filter out all duplicate values in nums array.
#The time for this will be O(n) because everything must be added to the set
#The space for this will be O(n) too which will happen if every value is added to the set.
#This is optimal because we must look at every value in nums anyway, but with the set we only have to convert the nums array to a set and compare the lengths. This will be the fastest rather than having to use multiple iterators.
class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)