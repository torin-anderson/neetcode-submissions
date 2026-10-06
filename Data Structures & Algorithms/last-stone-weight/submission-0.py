#We want to find the two highest values of the stones and each time subtract the second from the first
#A brute force solution would involve iterating through stones constantly until we run out of values, but that would be O(N^2)
#A better solution involves utilizing a max heap. We can convert stones into a max heap and while the heap has mroe than 1 one values we can keep popping from the max heap and if the heaviest stone is heavier than the second add that back to the heap
#This will take O(nlogn) because we have to go through all of sotnes to convert to a heap and it will take logn time to get down to 0 or 1 value
#Space is O(n) because the heap is starting as the same size as stone

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
        if stones:
            return abs(stones[0])
        else:
            return 0
        