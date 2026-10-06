#One solution would involve a two pointer where we have two iterators and find the product of the rest of the vlaues, but this would be O(n^2) and not optimal
#A more optimal solution should only involve a specific number of passes.
#My idea is that we can pass through this array twice. One pass through we can find the prefix products, or the product of ever value before the current index. Then we pass through a second time and find the suffix product by passing through the inputted array in reverse. We can just multiply this by the already found suffix value.
#The time for this will be O(n) because O(2n) simplifies to O(n)
#The space for this is O(n) because we will create our output, same length as nums, and two values which are constant space.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf = 1,1
        output = [1] * len(nums)
        for num in range(len(nums)):
            output[num] = pre
            pre *= nums[num]

        for num in range(len(nums)-1, -1,-1):
            output[num] = output[num]* suf
            suf *= nums[num]
        
        return output