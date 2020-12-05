def max_profit(A):
    if(len(A) < 2):
        return 0
    else:
        maxP = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                if(A[j] - A[i] > maxP):
                    maxP = A[j] - A[i]
    return maxP


#O (n log (n))

def recursive_profit(A):
    if(len(A) < 2):
        return 0
    length = len(A) // 2
    left = A[ : length]
    right = A[length : ]

    leftGood = recursive_profit(left)
    rightGood = recursive_profit(right)

    local_profit = (find_max(right) - find_min(left))

    return max(leftGood, rightGood, local_profit)




def find_min(A):
    min = 99999999
    for x in A:
        if (x < min):
            min = x
    return min


def find_max(A):
    max = -99999999
    for x in A:
        if (x > max):
            max = x
    return max


A = [310, 315, 275, 295]
#print(recursive_profit(A))

#O(n)

def dynamic(A):
    min = 9999999
    profit = -9999999
    for number in A:
        if (number < min):
            min = number
        if(number - min > profit):
            profit = number - min
    return profit

print(dynamic(A))