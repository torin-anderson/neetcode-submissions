#Find if the two strings have the same characters and number of characters
#So the lengths must be equal to start
#One approach would be to have multiple iterators where we have one going through s and then one subsequently going through t to find the character. This would miss duplicates however and would be a poor time of O(n^2)
#A much more optimal approach will involve a hashmap. We can keep a hashmap of the occurences of characters in s, and another one for t, and then compare the two hashmaps to see if they are the same. If so return true, else false
#TIme will be O(n) where n is the length of s AND t. We msut go through each character of both to add them to a hashmap.
#Space will also be O(n) because if all characters of both strings are unique we msut add each one
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)