class Solution:
    def longestPalindrome(self, s: str) -> str:

        bestL = 0 
        bestR = 0
        
        for i in range(len(s)):

            #ODD
            L = R = i
            while(L - 1 >= 0 and R + 1 <= len(s) - 1 and s[L - 1] == s[R + 1]):
                L -= 1
                R += 1
            if (R - L) > (bestR - bestL):
                bestL = L
                bestR = R
            
            #EVEN
            L = i
            R = i + 1
            if i == len(s) - 1 or s[L] != s[R]:
                continue
            while(L - 1 >= 0 and R + 1 <= len(s) - 1 and s[L - 1] == s[R + 1]):
                    L -= 1
                    R += 1

            if (R - L) > (bestR - bestL):
                bestL = L
                bestR = R
        
        return s[bestL:bestR + 1]

