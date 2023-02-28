class Solution:
    def getKthElement(self, firstArr: List[int], secondArr: List[int], k: int) -> int:
        # add your logic here

        firstArr.extend(secondArr)
        firstArr.sort()

        return firstArr[k - 1]
