#To solve this, we can utilize a heap
#We can use a min heap and what we can do is heapify the nums and iterate and pop until we reach the kth largest element and once we do we return that value
#This will be O(n) because we will be transforming nums into a heap and may have to iterate through the whole nums again
#Space is also O(1) because we will not have to make any new data structures

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        oneBeforeTarget = len(nums) - k
        for i in range(oneBeforeTarget):
            heapq.heappop(nums)

        return heapq.heappop(nums)