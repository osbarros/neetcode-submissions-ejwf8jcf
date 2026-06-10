class Solution:
    def trap(self, height: List[int]) -> int:
        curSum = 0

        for i in range(0, len(height) - 1):
            L = i -1
            R = i + 1
            maxLeft = maxRight = 0

            while L >= 0:
                maxLeft = max(height[L], maxLeft)
                L -= 1

            while R < len(height):
                maxRight = max(height[R], maxRight)
                R += 1

            minWallHeight = min(maxLeft, maxRight)
            curSum += max(0, minWallHeight - height[i])

        return curSum
                
            

                

                

