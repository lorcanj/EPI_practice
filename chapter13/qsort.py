def sort(A, lo, hi):
    if lo < hi:
        pivot_position = sort_in_array(A, 0, len(A) - 1)
        sort(A, lo, pivot_position - 1)
        sort(A, pivot_position + 1, hi)
    
    


def sort_in_array(A, lo, hi):
    # we are choosing the pivot
    i = left
    j = right - 1
    pivot = right

    
        

p = [1, 4, 2, 9, 8, 11, 30, 0, 7]
print(sort(p, 0 ,len(p) - 1))