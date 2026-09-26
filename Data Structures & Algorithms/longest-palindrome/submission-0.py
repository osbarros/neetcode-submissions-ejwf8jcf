class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        longestPalindromeLength = 0
        hasAlreadyUsedOdd = False

        for f in freq:
            if freq[f] % 2 == 0:
                longestPalindromeLength += freq[f]
            elif not hasAlreadyUsedOdd:
                longestPalindromeLength += freq[f]
                hasAlreadyUsedOdd = True
            else:
                longestPalindromeLength += freq[f] - 1
            
        return longestPalindromeLength


