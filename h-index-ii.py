class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def checkValidityOfHIndex(index, arr):
            return arr[index] < len(arr) - index

        lptr = 0
        rptr = len(citations) - 1

        while lptr <= rptr:
            mptr = lptr + (rptr - lptr) // 2

            if checkValidityOfHIndex(mptr, citations):
                lptr = mptr + 1
            else:
                rptr = mptr - 1

        return len(citations) - lptr