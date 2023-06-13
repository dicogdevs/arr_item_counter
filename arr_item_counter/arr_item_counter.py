def arr_item_counter(arr: list, left: int = 0, right: int = None):
    if not right:
        right = len(arr)
    
    if left >= right:
        return 0
    
    elif (right - left)  == 1:
        return 1
    
    elif (right - left)  == 2:
        return 2
    
    else:
        mid = (left + right) // 2
        return arr_item_counter(arr, left, mid) + 1 + arr_item_counter(arr, mid+1, right)
