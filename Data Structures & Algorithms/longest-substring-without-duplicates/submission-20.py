class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        L = R = curAmount = 0
        maxAmount = 1
        visited = set()
        
        for i in range(len(s)):
            while  R < len(s) and s[R] not in visited:
                visited.add(s[R])
                curAmount += 1
                print(f"Adding {s[R]} to visited, currentAmount = {curAmount}")
                R += 1
                
            maxAmount = max(maxAmount, curAmount)

            while R < len(s) and L <= R and s[R] in visited:
                visited.discard(s[L])
                curAmount -= 1
                print(f"Removing {s[L]} to visited, currentAmount = {curAmount}")
                L += 1           
        
        return maxAmount if len(s) > 0 else 0

