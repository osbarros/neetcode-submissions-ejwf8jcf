class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
        notDigits = {"D", "C", "+"}

        for op in operations:
            if op not in notDigits:
                value = int(op)
                record.append(value)
                result += value

            elif op == '+':
                value = record[-1] + record[-2]
                record.append(value)
                result += value

            elif op == 'C':
                value = record.pop()
                result -= value

            elif op == 'D':
                value = record[-1] * 2
                record.append(value)
                result += value

        return result