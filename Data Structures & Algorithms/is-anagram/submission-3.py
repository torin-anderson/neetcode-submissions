class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}
        for x in range(len(s)):
            iterS = s[x]
            if iterS not in countS:
                countS[iterS] = 1
            else:
                countS[iterS] += 1
            iterT = t[x]
            if iterT not in countT:
                countT[iterT] = 1
            else:
                countT[iterT] += 1
        
        return countS == countT