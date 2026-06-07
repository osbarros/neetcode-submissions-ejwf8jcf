class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
        notDigits = {"D", "C", "+"}
        for i in range(len(operations)):
            op = operations[i]
            if op not in notDigits:
                record.append(int(op))
                result += int(op)
            if op == '+':
                previous2 = record[-1] + record[-2]
                record.append(previous2)
                result += previous2
            if op == 'C':
                if len(record) > 0:
                    inv = record.pop()
                    result -= inv
            if op == 'D':
                record.append(record[-1] * 2)
                result += record[-1]
        return result
