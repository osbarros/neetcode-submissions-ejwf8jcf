class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        L = R = 0
        maxAmount = 1
        visited = set()
        
        while R < len(s):
            if s[R] not in visited:
                visited.add(s[R])
                print(f"Adding {s[R]} to visited, currentAmount = {R - L + 1}")
                R += 1
                maxAmount = max(maxAmount, (R - L))
            else:
                visited.discard(s[L])
                print(f"Removing {s[L]} to visited, currentAmount = {R - L + 1}")
                L += 1 
                     
        
        return maxAmount if len(s) > 0 else 0

