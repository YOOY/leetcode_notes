def myPow(x, n):
    if n < 0:
        result = x = 1/x
        n = -n
    elif n > 0:
        result = x
    else:
        return 1
    tmp = 1
    while n > 1:
        if n % 2 == 0:
            result *= result
            n >>= 1
        else:
            tmp *= result
            n -= 1
    result *= tmp
    return result

print(myPow(2.00, 10))