class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromicSubstrings = 0

        
        for i in range(len(s)):
            #ODD
            L = R = i
            while ((L >= 0) and (R < len(s)) and s[L] == s[R]):
                palindromicSubstrings += 1
                L -= 1
                R += 1

            #EVEN
            L = i
            R = i + 1
            while ((L >= 0) and (R < len(s)) and s[L] == s[R]):
                palindromicSubstrings += 1
                L -= 1
                R += 1

        return palindromicSubstrings