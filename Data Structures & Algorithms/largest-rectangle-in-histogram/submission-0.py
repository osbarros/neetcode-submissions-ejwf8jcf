class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largestArea = 0

        heights.append(0)

        for i in range(len(heights)):
            
            while stack and heights[stack[-1]] >= heights[i]:

                right = i
                height = heights[stack.pop()]
                left = 0
                if not stack:
                    left = -1
                else:
                    left = stack[-1]

                
                width = right - left - 1
                area = width * height
                largestArea = max(area, largestArea)

            stack.append(i)

        return largestArea