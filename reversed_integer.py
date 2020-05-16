#Given a 32-bit signed integer, reverse digits of an integer.

def reverse():                                         #define a function that takes an integer as an argument.
    x = int(input("Enter a number to reverse "))
    if x < 0:                                           #handle the case for a negative integer
        x = int("-" + str(abs(x))[::-1].lstrip("0"))    #converting the int into a str for slicing, then back to int
    elif x > 0:                                         #handle the case for positive integers
        x = int(str(x)[::-1].lstrip("0"))               #repeat the conversions and strip for trailing left zeros
    if abs(x) < 2**31:                                  #check for 32-bit int overflow
        print(x)
    else:
        print(0)
reverse()
            

