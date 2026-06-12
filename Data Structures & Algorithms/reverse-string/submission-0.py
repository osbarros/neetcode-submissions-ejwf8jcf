class Solution:
    def reverseString(self, s: List[str]) -> None:
        R = len(s) - 1
        L = 0

        while L < R:
            print(f"L = {L}; s[L] = {s[L]}")
            print(f"R = {R}; s[R] = {s[R]}")
            tmp = s[L]
            s[L] =  s[R]
            s[R] = tmp
            R -= 1
            L  += 1
        