# worst case is O(n)
# can do O (log n) I think


def first_instance(sorted_list, key):
    index = -1
    if sorted_list is None:
        return index
    
    lo = 0
    hi = len(sorted_list) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sorted_list[mid] == key:
            index = mid
            break
        elif key < sorted_list[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    if index == -1:
        return index
    else:
        while sorted_list[index] == key and index >= 0:
            index -= 1
        return index + 1 

# try to write this for O(log n)
# written for O(log n) and the worst case and best case is the same because it does a full thing
# each time. But better because discarding the RHS because only interested in the key or lower to find
# the first instance
def f_instance(sorted_list, key):
    index = -1
    if sorted_list is None:
        return index
    
    lo = 0
    hi = len(sorted_list) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sorted_list[mid] == key:
            index = mid
            hi = mid - 1
        elif key < sorted_list[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return index



l = [0, 1, 8, 12, 23, 23, 70, 70, 70, 70, 80, 90, 111]

print(f_instance(l, 70))