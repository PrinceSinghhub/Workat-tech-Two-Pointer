from collections import Counter


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        mydic = Counter(A)

        ans = mydic.keys()
        return len(ans)





