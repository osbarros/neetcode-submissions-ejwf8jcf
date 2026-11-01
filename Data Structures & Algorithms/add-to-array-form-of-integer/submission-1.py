class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        i = len(num) - 1

        while i >= 0 or k > 0 or carry > 0:
            valueK = k % 10
            valueNum = num[i] if i >= 0 else 0

            total = valueK + valueNum + carry

            digit = total % 10
            carry = total // 10

            if i >= 0:
                num[i] = digit
            else:
                num.insert(0, digit)

            k //= 10
            i -= 1

        return num