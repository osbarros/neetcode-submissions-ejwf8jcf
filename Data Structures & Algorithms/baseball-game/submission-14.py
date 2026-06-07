class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = deque(maxlen=3)
        result = 0
        notDigits = {"D", "C", "+"}
        for i in range(len(operations)):
            op = operations[i]
            if op not in notDigits:
                record.append(int(op))
                result += int(op)
            if op == '+':
                if len(record) >= 2:
                    previous2 = record[-1] + record[-2]
                elif len(record) == 1: 
                    previous2 = record[-1]
                else:
                    previous2 = 0
                record.append(previous2)
                result += previous2
            if op == 'C':
                if len(record) > 0:
                    inv = record.pop()
                    result -= inv
            if op == 'D':
                record.append(record[-1] * 2)
                result += record[-1]
            print(f"Op: {op}, Result: {result}, record: {record}")
        return result
