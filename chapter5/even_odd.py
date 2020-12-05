def even_odd(A):
    next_even = 0
    next_odd = len(A) - 1
    while(next_even != next_odd):
        if (A[next_even] & 1 == 0):
             next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

A = [1, 7, 2, 4, 9]
even_odd(A)
print(A)