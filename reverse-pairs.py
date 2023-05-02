class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def merge(left, right):
            lptr = 0
            rptr = 0

            ans = []

            while lptr < len(left) or rptr < len(right):
                if lptr < len(left) and rptr < len(right):
                    if left[lptr] <= right[rptr]:
                        ans.append(left[lptr])
                        lptr += 1
                    else:
                        ans.append(right[rptr])
                        rptr += 1
                elif lptr < len(left):
                    ans.append(left[lptr])
                    lptr += 1

                elif rptr < len(right):
                    ans.append(right[rptr])
                    rptr += 1
            return ans

        def mergeSortCustom(arr, l, r):
            nonlocal count
            if l == r:
                return [arr[l]]

            m = l + (r - l) // 2

            left = mergeSortCustom(arr, l, m)
            right = mergeSortCustom(arr, m+1, r)

            lptr = 0
            rptr = 0

            while lptr < len(left) and rptr < len(right):
                if left[lptr] > 2 * right[rptr]:
                    count += len(left) - lptr
                    rptr += 1
                else:
                    lptr += 1

            # print('the count has been updated to', count)

            return merge(left, right)

        mergeSortCustom(nums, 0, len(nums)-1)
        return count