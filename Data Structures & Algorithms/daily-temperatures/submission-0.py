class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n

        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                indexPopped = stack.pop()
                output[indexPopped] = i - indexPopped

            stack.append(i)

        return output