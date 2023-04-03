class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
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

            lptr = len(left) - 1
            rptr = len(right) - 1


            while lptr >=0 and rptr >=0:
                if right[rptr] >= left[lptr] - diff:
                    count += lptr + 1
                    rptr -= 1
                else:
                    lptr -= 1


            return merge(left, right)

        mergeSortCustom([nums1[i] - nums2[i] for i in range(len(nums1))], 0, len(nums1)-1)
        return count