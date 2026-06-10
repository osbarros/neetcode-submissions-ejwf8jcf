class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        L = R = curAmount = 0
        maxAmount = 1
        visited = set()
        
        for R, c in enumerate(s):
            print(c)
            while  R < len(s) and s[R] not in visited:
                visited.add(s[R])
                curAmount += 1
                R += 1
                
                

            L += 1
            R = L + 1
            maxAmount = max(maxAmount, curAmount)
            curAmount = 0
            visited.clear()

        return maxAmount if len(s) > 0 else 0

