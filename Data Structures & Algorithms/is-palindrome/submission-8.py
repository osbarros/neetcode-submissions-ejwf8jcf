class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while L < R:
            while not s[R].isalnum() and R > L:
                R -= 1
            while not s[L].isalnum() and L < R:
                L += 1
            
            if s[R].lower() != s[L].lower():
               return False
            R -= 1
            L += 1
        return True