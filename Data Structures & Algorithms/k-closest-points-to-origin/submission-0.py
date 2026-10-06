#My

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        wDistance = []
        for point in points:
            wDistance.append([math.sqrt(((0 - point[0])**2 + (0 - point[1])**2)), point[0], point[1]])
        heapq.heapify(wDistance)
		
        output = []
        for i in range(k):
            d,x,y = heapq.heappop(wDistance)
            output.append([x,y])
	
        return output