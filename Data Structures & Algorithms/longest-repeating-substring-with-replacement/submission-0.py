class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}

        currentHighest = 0
        output = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            currentHighest = max(currentHighest, count[s[right]])

            while (right-left + 1) - currentHighest > k:
                count[s[left]] -= 1
                left += 1
            
            output = max(output, right - left+1)

        return output