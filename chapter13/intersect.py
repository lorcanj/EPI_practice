# take two sorted lists as input and compute the intersection of
# the two lists
# my method above is better for the situation where the two lists are of similar size and relatively small

def intersect(list1, list2):
    if len(list1) > len(list2):
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1
    result_set = set()
    smaller_counter = 0
    longer_counter = 0

    while smaller_counter < len(shorter) - 1 and longer_counter < len(longer) - 1:
        while shorter[smaller_counter] < longer[longer_counter]:
            smaller_counter += 1
        while longer[longer_counter] > shorter[smaller_counter]:
            longer_counter += 1
        result_set.add(shorter[smaller_counter])
        check = shorter[smaller_counter]
        while smaller_counter != len(shorter) - 1 and shorter[smaller_counter] == check:
            smaller_counter += 1

        print(shorter[smaller_counter])
    return result_set



# solution taken from the book is the below:
def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if a in B and (i == 0 or a != A[i - 1])]
    # this second part is checking the output array and if it will be the first
    # element in the array then it can be added or because it's sorted, if it 
    # were to be a duplicate, then the duplicate will be the last element in that
    # array

# can take advantage of binary search for looking for the number in the other array

# if both of the arrays are of a similar length, then can check


l = [1, 2, 2, 3, 4, 5, 5, 5]
l2 = [0, 2, 2, 8, 9]
result = intersect_two_sorted_arrays(l, l2)
print(result)