#Luiz Gouvea
#17/02/2025
#divisors

def divisors(n):
    my_divisors_list = []
    for i in range(1, n):
        if n % i == 0:
            my_divisors_list.append(i)
    return my_divisors_list 

def main():
    print(divisors(30))

main()


