
def sort(arr, order):
    arrLen = len(arr)
    if arrLen < 2:
        return arr

    middle = arrLen // 2
    l_arr = sort(arr[:middle], order)
    r_arr = sort(arr[middle:], order)

    return merge(l_arr, r_arr, order)

def merge(l_arr, r_arr, order):
    res = []
    i = j = 0
    
    if order == 'asc':
        orderCoeff = 1
    elif order == 'desc':
        orderCoeff = -1
    else:
        assert False, 'incorrect order'

    while i < len(l_arr) and j < len(r_arr):

        if orderCoeff * l_arr[i] < orderCoeff * r_arr[j]:
            res.append(l_arr[i])
            i += 1
        else:
            res.append(r_arr[j])
            j += 1
        
    res.extend(l_arr[i:])
    res.extend(r_arr[j:])

    return res