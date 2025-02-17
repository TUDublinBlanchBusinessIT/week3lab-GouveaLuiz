#Luiz Gouvea
#17/02/2025
#perfectNumber

from divisors import divisors

def isPerfectNumber(n):
    if sum(divisors(n)) == n:
        return True
    return False  

print(isPerfectNumber(8128))


