#Skip over non alphanumberic characters
#palindrome if both sides of the string are equal
#My solution involves a two pointer method where we start left at the start of the string and right at the end. We first check to see if the characters at the current index are alphanumeric, if not skip them. Then we check to see if the left and right characters are equal. If not then return false. If true we keep going until while left < right, otherwise we return true.
#The time is O(n) becasue we go through the string once
#The space is O(1) because we don't need much extra space, jsut a couple of constant size variables
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.checkChar(s[left]):
                left += 1
            while left < right and not self.checkChar(s[right]):
                right -=1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

    def checkChar(self, c) -> bool:
        return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')