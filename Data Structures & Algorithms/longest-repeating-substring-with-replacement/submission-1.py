class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counting_repeated = {}
        R = L = 0
        last_char = ''
        max_lenght = 1
        max_freq = 0

        for R in range(len(s)):

            
            counting_repeated[s[R]] = counting_repeated.get(s[R], 0) + 1

            max_freq = max(counting_repeated.values())

            
            

            if (R - L + 1) - max_freq > k:
                counting_repeated[s[L]] = counting_repeated[s[L]] - 1
                L += 1

            max_lenght = max((R - L + 1), max_lenght)

        return max_lenght

