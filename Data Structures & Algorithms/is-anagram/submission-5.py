class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for x in range(len(s)):
            iterS = s[x]
            if iterS not in count:
                count[iterS] = 1
            else:
                count[iterS] += 1
            iterT = t[x]
            if iterT not in count:
                count[iterT] = -1
            else:
                count[iterT] -= 1
        
        return all(x==0 for x in count.values())