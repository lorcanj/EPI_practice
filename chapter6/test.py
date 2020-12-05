from functools import reduce
import string
def string_to_int(s):
    return reduce(
        lambda runningsum, c: runningsum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0)

print(string_to_int("12345"))


print(string.digits.index("8"))