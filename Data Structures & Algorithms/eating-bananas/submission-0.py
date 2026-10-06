#We are trying to find the minimum eating rate that fits within h
#When finding an eating rate we will need to calculate the ceiling to determine hours
#The maximum of piles will always be successful, but not the answer we want typically to be honest.
#Since we are searching for this minimum eating rate, we should utilize a binary search. We can have the left bound be 1, and then the right bound be the max. We can then binaryily search values and check how they do when iterating through the whole list. If the hours it takes for the current checking value is less than or equal to h then we can change r to middle - 1. If greater than h we can change l to middle + 1
#The time will be O(n times logm) because maximum will take n time looking through piles and we are going to be going through piles each time checking the current value and logm where m is the length of the max from piles because we are doing binary search through the values of the max
#The space will be O(1) because we are only saving a couple of constant time variables
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        output = r

        while l <= r:
            m = (l+r) //2
            
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / m)

            if totalTime > h:
                l = m + 1
            else:
                output = m
                r = m - 1
        return output
        