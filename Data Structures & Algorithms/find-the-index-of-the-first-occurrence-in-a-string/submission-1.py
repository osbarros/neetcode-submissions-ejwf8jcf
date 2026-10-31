class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        L = 0
        R = 0

        while R < len(haystack):

            print(f"Iteration {L + 1}")

            print(f"L = {L}")
            print(f"R = {R}")
            
            for i in range(len(needle)):

                if R >= len(haystack):
                    return -1

                if haystack[R] == needle[i]:
                    if i == len(needle) - 1:
                        return L

                    else:
                        R += 1

                else:
                    print("else")
                    break
                            

            
            L += 1
            R = L 

        return -1