class Solution:
    def mergeSortedArrays(self, A: List[int], B: List[int]) -> List[int]:

        if len(A) == 0:
            return B
        if len(B) == 0:
            return A

        for i in range(len(A)):
            if A[i] > B[0]:
                temp = A[i]
                A[i] = B[0]
                B[0] = temp
                B.sort()

        return A + B


class Solution:
    def mergeSortedArrays(self, A: List[int], B: List[int]) -> List[int]:

        A[:] = A+B
        A.sort()
        return A

