#Luiz Gouvea
#17/02/2025
#findFirstFourPNs

from perfectNumber import isPerfectNumber

def find_first_four_perfect_numbers():
    count = 0
    num = 1
    while count < 4:
        if isPerfectNumber(num):
            print(f"{num} is a perfect number")
            count += 1
        num += 1  

find_first_four_perfect_numbers()

