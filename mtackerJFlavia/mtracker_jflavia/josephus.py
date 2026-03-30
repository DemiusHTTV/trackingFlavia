def IosifeFlavia(arr,n,k):
    if len(arr) == 1:
        return arr[0]
    else:
        index = (k-1) % len(arr)
        arr.pop(index)
        return IosifeFlavia(arr,n,k)
    
