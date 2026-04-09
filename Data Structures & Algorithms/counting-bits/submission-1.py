class Solution:
    def countBits(self, n: int) -> List[int]:
        number = 0
        list_counts = list()
        while number <= n:
            count = 0
            tmp_number = number
            while tmp_number > 0:
                if (tmp_number & 1) == 1:
                    count += 1
                tmp_number = tmp_number >> 1
            list_counts.append(count)
            number += 1
        
        return list_counts
