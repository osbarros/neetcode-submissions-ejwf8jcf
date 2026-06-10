class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        isPalindrome = True
        secondChanceR = 0
        secondChanceL = 0

        while L < R:
            if s[R] != s[L]:
                secondChanceR = R
                secondChanceL = L
                isPalindrome = False
                break
            
            L += 1
            R -= 1
        
        if isPalindrome == True:
            return True
        
        isPalindrome = True

        print(f"second chance L: {secondChanceL}")
        print(f"second chance R: {secondChanceR}")
        
        L = secondChanceL + 1
        R = secondChanceR

        while L < R:
            print(s[R] , s[L])
            if s[R] != s[L]:
                isPalindrome = False
                break 
            L += 1
            R -= 1

        if isPalindrome == True:
            return True 

        isPalindrome = True   
        L = secondChanceL
        R = secondChanceR - 1

        while L < R:
            if s[R] != s[L]:
                isPalindrome = False
                break 
            L += 1
            R -= 1
            
        return isPalindrome
                








