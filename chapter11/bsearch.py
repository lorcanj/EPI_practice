def b_search(l, key):
    lo = 0
    hi = len(l) - 1
    mid = hi // 2
    while hi > lo:
        if key == l[mid]:
            return True
        elif key > l[mid]:
            lo = mid + 1
            mid += (hi - lo) // 2
        else:
            hi = mid - 1
            mid -= (hi - lo) // 2
    return False


#improvement

def BSear(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1 

l = [0, 2, 4, 5, 6, 8, 22, 34, 42, 48, 60, 70, 80]
print(b_search(l, 47))



