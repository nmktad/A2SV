class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1

        lptr = 0
        rptr = 1

        maxlen = 0
        runninglen = 0

        shouldBeGreater = True if arr[lptr] > arr[rptr] else False

        while rptr < len(arr) and lptr < rptr:
            # print(f"comparing {arr[lptr]} and {arr[rptr]} shouldbegreater is {shouldBeGreater} maxlen found is {maxlen} and runninglen is {runninglen}")
            if shouldBeGreater:            
                if arr[lptr] > arr[rptr]:
                    runninglen += 1
                    lptr = rptr
                    rptr = lptr + 1
                    shouldBeGreater = not shouldBeGreater
                    maxlen = max(maxlen, runninglen + 1)

                else:
                    shouldBeGreater = True if arr[lptr] > arr[rptr] else False
                    maxlen = max(maxlen, runninglen + 1)
                    runninglen = 0

                    if arr[lptr] == arr[rptr]:
                        if rptr < len(arr) - 1:
                            rptr += 1
                            lptr += 1
                        elif rptr + 1 == len(arr):
                            maxlen = max(maxlen, runninglen + 1)
                            break
            else:
                if arr[lptr] < arr[rptr]:
                    runninglen += 1
                    lptr = rptr
                    rptr = lptr + 1
                    shouldBeGreater = not shouldBeGreater
                    maxlen = max(maxlen, runninglen + 1)

                
                else:
                    shouldBeGreater = True if arr[lptr] > arr[rptr] else False
                    maxlen = max(maxlen, runninglen + 1)
                    runninglen = 0

                    if arr[lptr] == arr[rptr]:
                        if rptr < len(arr) - 1:
                            rptr += 1
                            lptr += 1
                        elif rptr + 1 == len(arr):
                            maxlen = max(maxlen, runninglen + 1)
                            break
                shouldBeGreater = True

        return maxlen