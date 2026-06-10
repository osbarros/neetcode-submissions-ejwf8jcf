class Solution:
    def trap(self, height: List[int]) -> int:
        curSum = 0
        lenHeight = len(height)
        maxLeft = [0] * lenHeight
        maxRight = [0] * lenHeight

        maxLeft[0] = height[0]
        for i in range(1, lenHeight):
            maxLeft[i]= max(maxLeft[i - 1], height[i])
        
        maxRight[lenHeight - 1] = height[lenHeight - 1]

        for j in range(lenHeight - 2, -1, -1):
            maxRight[j] = max(maxRight[j + 1], height[j])

            

        for k in range(1, lenHeight):
            L = i -1
            R = i + 1

            minWallHeight = min(maxLeft[k], maxRight[k])
            curSum += max(0, minWallHeight - height[k])

        return curSum
                
            

                

                

