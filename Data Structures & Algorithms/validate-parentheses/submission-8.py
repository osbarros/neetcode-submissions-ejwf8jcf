class Solution:
    def isValid(self, s: str) -> bool:
        closing =  {'}', ')', ']'}
        opening = []
        for c in s:
            if c not in closing:
                opening.append(c)
            else:
                last = opening[-1] if len(opening) > 0 else  ''
                if last == '{' and c == '}':
                    opening.pop()
                elif last == '(' and c == ')':
                    opening.pop()
                elif last == '[' and c == ']':
                    opening.pop()
                else: 
                    return False
        return len(opening) == 0
