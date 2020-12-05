def quicksort(A, lo, hi):
    #pivot is defined here and then passed
    pivot = A[0]
    while lo < hi:
        if A[lo] < pivot:
            lo += 1
        if A[hi] > pivot:
            hi += 1
        if A[lo] > pivot and A[hi] < pivot:
            A[lo], A[hi] = A[hi], A[lo]
    
    
    



# want the partitioning to be done recursively first
def partition(A, lo, hi):
    if len(A) < 2:
        return A
    partition(A, lo, pivot - 1)
    partition(A, pivot + 1, hi)
    quicksort(A)
