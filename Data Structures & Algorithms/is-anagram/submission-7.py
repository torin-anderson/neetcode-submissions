class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for x in range(len(s)):
            iterS = s[x]
            iterT = t[x]
            count[ord(iterS) - ord('a')] += 1
            count[ord(iterT) - ord('a')] -= 1
        
        return all(x==0 for x in count)