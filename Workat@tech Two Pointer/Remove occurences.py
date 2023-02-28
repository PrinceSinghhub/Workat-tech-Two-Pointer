class Solution:
    def removeOccurences(self, A: List[int], k: int) -> int:
        
        while k in A:
            A.remove(k)

        return len(A)

    # add your logic here



