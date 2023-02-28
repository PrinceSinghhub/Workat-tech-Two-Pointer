class Solution:
    def hasTwoSumZero(self, A: List[int]) -> bool:

        start = 0
        end = len(A) - 1

        while start < end:
            if A[start] + A[end] == 0:
                return True
            if A[start] + A[end] > 0:
                end -= 1
            else:
                start += 1

        return False



