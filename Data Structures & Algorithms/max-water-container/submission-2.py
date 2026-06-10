class Solution:

    def maxArea(self, heights: List[int]) -> int:
        
        L = 0
        R = len(heights) - 1

        curA = maxA = 0

        while L < R: 
            curA = (R - L) * min(heights[R], heights[L])
            maxA = max(curA, maxA)
            if heights[R] < heights[L]:
                R -= 1
            
            else:
                L += 1
    

        return maxA
