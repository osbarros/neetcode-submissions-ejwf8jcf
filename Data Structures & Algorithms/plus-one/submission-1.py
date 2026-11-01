class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            total = 0
            if i == len(digits) - 1:
                total = digits[i] + 1
            else: 
                total = digits[i] + carry
            digit = total % 10
            carry = total // 10
            
            digits[i] = digit

        if carry > 0:
            digits.insert(0, carry) 

        return digits       


            