#return k most frequent elements
#Have to keep track of how often values are in nums array
#This seems like the best case for use of a hashmap
#Also seems like a good situation for a bucket sort
#What we can do is establish a bucket sort technique. We will start by creating a hashmap that counts the appearance of an int in nums. Then we will create a list of lists and go through the hashmap. Based on the appearance value add it to the list of list's index for the appearance value. Then we go through this bucket sort in reverse and return the k most frequent numbers
#The time for this willinvolve going through nums once, then the hashmap once, then could go through the bucket sorted array once. This could be O(3n) which will simplify to O(n)
#The space is going to be O(2n) because of the hashmap and the lsit of lists, but this simplifies to O(n) also.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}
        for num in nums:
            if num in occur:
                occur[num] += 1
            else:
                occur[num] = 1

        buckets = [[] for i in range(len(nums)+1)]
        for key, value in occur.items():
            buckets[value].append(key)
        

        output = []
        for val in range(len(buckets)-1, -1, -1):
            if buckets[val]:
                for i in buckets[val]:
                    output.append(i)
                    if len(output) == k:
                        return output
        