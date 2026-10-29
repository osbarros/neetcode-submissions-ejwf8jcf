class Solution:
    def trap(self, height: List[int]) -> int:
        
        amountWater = 0
        stack = []
        for i in range(len(height)):


            while stack and height[stack[-1]] < height[i]:

                rightWall = i
                valley = stack.pop()

                
                if not stack:
                    break
                leftWall = stack[-1]



                width = rightWall - leftWall - 1

                h = min(height[rightWall], height[leftWall]) - height[valley]


                amountWater += width * h


            stack.append(i)

        return amountWater