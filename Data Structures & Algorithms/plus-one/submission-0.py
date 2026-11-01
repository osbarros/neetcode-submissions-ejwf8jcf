class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        output = deque()
        for i in range(len(digits) - 1, -1, -1):
            total = 0
            if i == len(digits) - 1:
                total = digits[i] + 1
            else: 
                total = digits[i] + carry
            if total >= 10:
                digit = total - 10
                carry = 1
            else:
                digit = total
                carry = 0

            output.appendleft(digit)

        if carry > 0:
            output.appendleft(carry) 

        return list(output)       


            