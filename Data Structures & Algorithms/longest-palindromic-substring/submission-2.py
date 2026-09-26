class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestSubstring = s[0]
        curSubstring = ""
        
        for i in range(len(s)):
            if len(curSubstring) > len(longestSubstring):
                longestSubstring = curSubstring
            if i == 0 or i == len(s) - 1:
                continue
            L = R = i
            curSubstring = s[R]
            while(True):
                if L - 1 >= 0 and R + 1 <= len(s) - 1 and s[L - 1] == s[R + 1]:
                    curSubstring = s[L - 1] + curSubstring + s[R + 1]
                    L -= 1
                    R += 1
                else:
                    break
            
        L = R = 0
        for i in range(len(s)):
            if len(curSubstring) > len(longestSubstring):
                longestSubstring = curSubstring
            L = i
            R = i + 1
            if i == len(s) - 1 or s[L] != s[R]:
                continue

            curSubstring = s[L] + s[R]
            
            while(True):
                if L - 1 >= 0 and R + 1 <= len(s) - 1 and s[L - 1] == s[R + 1]:
                    curSubstring = s[L - 1] + curSubstring + s[R + 1]
                    L -= 1
                    R += 1
                else:
                    break
        
        return longestSubstring

