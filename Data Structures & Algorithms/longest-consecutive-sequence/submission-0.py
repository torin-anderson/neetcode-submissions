#need to find longest consecutive order of vlaues in a list
#must be O(n) so no sorting
#How we can think about this is through sequences. We can have both a set version of nums and then iterate through nums. While iterating through nums, we can look to see if the current value is a start of the sequence by seeing if num -1 is in the set, which is O(1). Then we can keep adding one to num and seeing if the next value is in the nums set. We'll keep track of the longest sequence through a maxSequence counter.
#The time for this will be O(n) because we go through nums once.
#The space for this is O(n) because we will be converting nums to a set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        highestSequence = 0

        for num in nums:
            if num-1 not in numsSet:
                sequence = 1
                currentVal = num + 1
                while num + sequence in numsSet:
                    sequence += 1
                highestSequence = max(highestSequence, sequence)

        return highestSequence