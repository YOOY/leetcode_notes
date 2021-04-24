# 

def divide(dividend, divisor):
    maximum = 2**31 - 1
    minimum = -2**31

    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    
    while dividend >= divisor:
        sum = divisor
        rep = 1
        # to double divisor
        while dividend > sum + sum:
            sum += sum
            rep += rep
        dividend -= sum
        count += rep
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        count = 0 - count
    if count < minimum:
        count = minimum
    if count > maximum:
        count = maximum
    return count

print(divide(10,3))


def divide_bit_operation(dividend, divisor):
    maximum = 2**31 - 1
    minimum = -2**31
    count = 0
    positive = (dividend < 0) is (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor:
        i = 0
        while dividend > divisor << (i+1):
            i += 1
        count += (1 << i)
        dividend -= (divisor << i)
    if not positive:
        count = 0 - count
    if count > maximum:
        count = maximum
    if count < minimum:
        count = minimum
    return count

print(divide_bit_operation(10, 3))