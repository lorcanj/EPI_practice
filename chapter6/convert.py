

a = 1
print(chr(ord('0') + 42 % 10))

def intToString(number):
    array = []
    while (number != 0):
        last_digit = number % 10
        array.append(str(last_digit))
        number -= last_digit
        number =  number // 10
    return ''.join(array)

a = 1234567
b = intToString(a)
#print(b)

def stringToInt(string):
    array = []
    for x in string:
        a = ord(x)
        a -= 48
        array.append(str(a))
    word = ''.join(array)
    print(word)
    return(''.join(array))



#print("hi")
#print(stringToInt("98442"))

#a = intToString(123)
#print(type(a))


