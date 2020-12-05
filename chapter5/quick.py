import random

def quick(A, index):
    lower = []
    same = []
    higher = []
    for i in range(len(A)):
        if(A[i] < A[index]):
            lower.append(A[i])
        elif(A[i] == A[index]):
            same.append(A[i])
        else:
            higher.append(A[i])
    A = []
    A.extend(lower)
    A.extend(same)
    A.extend(higher)
    return A

#A = [70, 69, 4]
# [69, 70, 4] 
A = [random.randint(1, 100) for _ in range(10)]
#A = [10, 9, 8, 6]

for x in A:
    print(x)

print("")
#B = quick(A, 4)


# The above uses O(n) extra space in the creation of the two new lists
# could probably reduce this through swapping variables in place
# index = 2
def quickPlace(A, index):
    comparison = A[index]
    j = len(A) - 1
    lo = 0
    #write up the algorithm written in the book
    # need to alter this
    # finish this Q tomorrow and then read the solution
    while(j != lo):
        if(A[j] <  comparison):
            A[j], A[lo] = A[lo], A[j]
            lo += 1
        else:
            j -= 1
    checker = -1
    for i in range(len(A)):
        if(A[i] == comparison):
            checker = i
            break
    if(A[j] > comparison and j < checker):
        A[j], A[checker] = A[checker], A[j]
    elif (A[j] < comparison and j > checker):
        A[checker], A[j] = A[j], A[checker]
    return A
    


    print("This is the last thing {}".format(A[j]))
    return A
        
        

                

B = quickPlace(A, 1)

for x in B:
    print(x)
        

#if(lo < index):
#        if(A[lo] < comparison):
#            A[lo], A[index] = A[index], A[lo]
#    else:
#        if(A[lo] > comparison):
#            A[index], A[lo] = A[lo], A[index]
    