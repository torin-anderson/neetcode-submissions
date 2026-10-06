#Output is an array


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)-1):
            currentTemp = temperatures[i]
            count = 0

            for j in range(i+1, len(temperatures)):
                if currentTemp < temperatures[j]:
                    count = j - i
                    break

            output.append(count)
        output.append(0)
        return output