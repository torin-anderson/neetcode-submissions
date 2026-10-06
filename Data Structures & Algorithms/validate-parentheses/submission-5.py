from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        endingStrings = {')': "(", "]":"[", "}":"{"}
        stack = deque()
        if len(s) %2 == 1:
            return False
        else:
            for i in s:
                if i in endingStrings:
                    if stack and endingStrings[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
            return True if not stack else False