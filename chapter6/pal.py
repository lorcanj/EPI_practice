def palendromic(s):
    for i in range(len(s) // 2):
        if(s[i] != s[~i]):
            return False
    return True


def isPal(s):
    return all(s[i] == s[~i] for i in range (len(s) // 2))

print(isPal(""))

"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = []
for number in range(len(a)):
    b.append(~a[number])
    print(b[number])

"""

