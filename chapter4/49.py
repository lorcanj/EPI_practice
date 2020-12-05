import math


def pal(num):
    if(num < 0):
        return False
    if(num < 10):
        return True
    while not(num < 0):
        a = int(num % 10)
        b = int(math.log(num, 10))
        c = int(num / (10 ** b))
        if(not(a & c)):  
            return False
        num = num - (c * (10**b))
        num = (num - a) / 10
        if(num < 10):
            return True
    return True


    #Taken from the book

    def is_palindrome(x):
        if x <= 0:
            return x == 0

        num_digits = math.floor(math.log10(x)) + 1



    





