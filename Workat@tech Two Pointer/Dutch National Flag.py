class Solution:

    def swap(self, arr, ind1, ind2):

        temp = arr[ind1]
        arr[ind1] = arr[ind2]
        arr[ind2] = temp
        return arr

    def sortTheArray(self, A):
        low = 0
        mid = 0
        highe = len(A) - 1

        while mid <= highe:
            if A[mid] == 0:
                self.swap(A,low, mid)
                low += 1
                mid += 1

            elif A[mid] == 1:
                mid += 1

            elif A[mid] == 2:
                self.swap(A, mid, highe)
                highe -= 1

        return A
ans = Solution()
arr = [1,0,1,2,2]
print(ans.sortTheArray(arr))



