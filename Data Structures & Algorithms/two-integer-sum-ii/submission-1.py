#We can use a two pointer solution since we want O(1) space
#Since we are guaranteed a solution we can start one pointer at the back and one at the front. Since this is non decreasing too then we can jsut check if the current sum is == to target, if greater than then move right down, if less than then move left up.
#Time is O(n) b/c may have to go through whole array
#Space is O(1) b/c just two variables being used
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]