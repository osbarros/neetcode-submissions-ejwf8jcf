class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        output = deque()
        carry = 0
        kStr = str(k)
        indexK = len(kStr) - 1
        indexNum = len(num) - 1
        
        while indexK >= 0 or indexNum >= 0:
            valueK = int(kStr[indexK]) if indexK >= 0  else 0
            valueNum = num[indexNum] if indexNum >= 0 else 0

            total = valueK + valueNum + carry

            digit = total % 10
            carry = total // 10

            output.appendleft(digit)
            
            indexNum -= 1
            indexK -= 1


        if carry > 0:
            output.appendleft(carry)

        return list(output)

