#We are returning an integer
#Longest substring without a duplicate
#How I see this, we can use a sliding window where we start left at 0 and right at 0, and then have a value for the highest sequence which we can start at one. We can iterate through s, which will represent the right,  and every time that left == right then we move the left one. Each iteration to we compare the max value and then r - l and whichever is higher is the max. Once r reaches the end we return the max
#Time is O(n) because at most we go through the entire array twice which simplifies to O(n)
#Space is O(1) because we are saving jsut a couple of constant sized variables
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        output = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]]+1)

            seen[s[r]] = r
            output = max(output, r - l + 1)
        return output