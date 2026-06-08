class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        R = L + k
        count = 0
        avg = 0
        sum_window = 0

        for i in range(R-L):
            sum_window += arr[i]
        
        avg = sum_window / k
        if avg >= threshold:
            count += 1
        
        L = 1

        while R < len(arr):
            print(f"range from {L} to {R}")
            sum_window = sum_window - arr[L-1] + arr[R]
            avg = sum_window/k
            print(avg)
            if avg >= threshold:
                count += 1
            R += 1
            L += 1
        
        return count
            