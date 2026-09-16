class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        possibleDigits = []
        if not digits:
            return possibleDigits
        currentCombination = ""
        lenDigits = len(digits)
        mapping = [
            [],                     # 0
            [],                     # 1
            ["a", "b", "c"],        # 2
            ["d", "e", "f"],        # 3
            ["g", "h", "i"],        # 4
            ["j", "k", "l"],        # 5
            ["m", "n", "o"],        # 6
            ["p", "q", "r", "s"],   # 7
            ["t", "u", "v"],        # 8
            ["w", "x", "y", "z"]    # 9
        ]
        iteration = 0

        def helper(i, currentCombination, mapping, possibleDigits):

            if len(currentCombination) == lenDigits:
                possibleDigits.append(currentCombination)
                return 
            
            
            
            for letter in (mapping[int(digits[i])]):
                currentCombination += letter
                helper(i + 1, currentCombination, mapping, possibleDigits)
                currentCombination = currentCombination [:-1]

        helper(0, currentCombination, mapping, possibleDigits)
        return possibleDigits

                














        