# check if n can be formed by 3**0 + 3**1 + ... + 3**n
# if any r equals to 2 it means we need 2 * (3 ** n) which should be false
def checkPowersOfThree(n):
    while n > 1:
        n, r = divmod(n, 3)
        if r == 2:
            return False
    return True

print(checkPowersOfThree(21))