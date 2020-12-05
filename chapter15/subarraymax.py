import itertools

#below doesn't really work for negative numbers

def highest_sub_array(A):
    if A is None:
        return []
    running_sum = global_max = A[0]
    for i in range(1, len(A)):
        if running_sum + A[i] > 0:
            running_sum += A[i]
        else:
            running_sum = 0
        if running_sum > global_max:
            global_max = running_sum
    return global_max

a = [-904, -40, -523, -12, -335, -385, -124, -481, -31]

"""
iterator = itertools.accumulate(a)
for _ in iterator:
    print(_)
#print(iterator)
"""

def find_maximum_sub(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
        
    return max_sum

print(find_maximum_sub(a))