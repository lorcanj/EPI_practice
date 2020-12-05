

def parity(num):
    result = 0
    while num:
        result ^= num & 1
        num >>= 1
    return result

x = 5
#print(parity(x))


def par(x):
    count = 0
    while x:
        x &= (x - 1)
        count ^= 1
    return count

#print(par(4))

def par_prop(x):
    