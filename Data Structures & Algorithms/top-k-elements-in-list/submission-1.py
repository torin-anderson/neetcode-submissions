from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []


        counter = Counter(nums)
        length = len(nums) 

        buckets = [[] for _ in range(length+1)]
        
        for key, count in counter.items():
            buckets[count].append(key)
        
        output = []
        
        for outer in range(len(buckets)-1, -1, -1):
            for inner in buckets[outer]:
                output.append(inner)
                k-=1
                if k == 0:
                    return output
        return output