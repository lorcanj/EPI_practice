def sort(A, lo, hi):
    if lo < hi:
        pivot_position = sort_in_array(A, lo, hi)
        sort(A, lo, pivot_position - 1)
        sort(A, pivot_position + 1, hi)    


def sort_in_array(A, lo, hi):

    # we are choosing the pivot as the element on the right-hand side
    # which can cause problems if the elements on the right are generally
    # greater than the elements on the left as it means that the pivot will be poor
    # and the time complexity degrades to O(n^2)
    i = lo
    j = hi - 1
    pivot = A[hi]

    while i < j:
        while A[i] < pivot and i < hi:
            i += 1
        while A[j] >= pivot and j > lo:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    
    if A[i] > pivot:
        A[i], A[hi] = A[hi], A[i]
    return i

p = [1, 4, 2, 9, 8, 11, 30, 0, 7]
for x in p:
    print(x)
print()
sort(p, 0 ,len(p) - 1)
for x in p:
    print(x)