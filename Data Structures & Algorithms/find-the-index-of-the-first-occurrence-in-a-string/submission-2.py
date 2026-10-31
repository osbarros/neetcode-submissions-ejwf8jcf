class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        L = 0
        R = 0

        while R < len(haystack):

            
            for i in range(len(needle)):

                if R >= len(haystack):
                    return -1

                if haystack[R] == needle[i]:
                    if i == len(needle) - 1:
                        return L

                    else:
                        R += 1

                else:
                    break
                            

            L += 1
            R = L 

        return -1