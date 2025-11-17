def binary_search(lst, value):
    lower = 0
    upper = len(lst) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] < value:
            lower = mid + 1
        elif lst[mid] > value:
            upper = mid - 1
        else:
            return True
    return False
