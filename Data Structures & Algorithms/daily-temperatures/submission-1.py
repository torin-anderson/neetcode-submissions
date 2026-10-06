#Output is an array



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                stackIndex, stackVal = stack.pop()
                output[stackIndex] = index - stackIndex 
            stack.append((index, val))
        
        return output