from collections import Counter


# worst case depends on the time complexity of the sort function
# but this is at least O(n) plus the time complexity of the sorted function
def check_pal(word):
    sort = ''.join(sorted(word))
    odd = 0
    count = 0
    for i in range(len(sort)):
        if i != (len(sort) - 1) and sort[i] != sort[i + 1]:
            count += 1
            if count & 1 == 1:
                odd += 1
                count = 0
            elif count == 0:
                odd += 1
            if odd > 1:
                return False
        else:
            count += 1
    return True


#for the below use a collections.counter

def pali(s):
    thing = Counter(s)
    return sum(v % 2 for v in thing.values()) <= 1 


s = 'llorcan'
#print(check_pal(s))
print(pali(s))