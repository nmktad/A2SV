for _ in range(int(input())):
    ltr = {}
    rtl = {}
    
    row, col = map(int , input().split())
    
    matrix = [list(map(int , input().split())) for x in range(row)]
    _max = 0
    
    for irow in range(row):
        for icol in range(col):
            pltr = irow + icol
            prtl = icol - irow
            ltr[pltr] = ltr.get(pltr , 0) + matrix[irow][icol]
            rtl[prtl] = rtl.get(prtl , 0) + matrix[irow][icol]
    
    for irow in range(row):
        for icol in range(col):
            pltr = icol + irow
            prtl = icol - irow
            _max = max(_max, ltr[pltr] + rtl[prtl] - matrix[irow][icol])
    
    print(_max)
