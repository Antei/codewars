def sum_array(arr):
    if arr == None or len(arr) < 2:
        return 0
    return sum(arr) - (min(arr) + max(arr))