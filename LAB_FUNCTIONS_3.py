# LAB LAB_FUNCTIONS_3


def is_prime(number : int) -> bool:
    if number <= 1:
        return False

    for n in range(2, number):
        if number%n == 0:
            return False
    
    return True



def find_primes(x:int , y:int) -> list:
    primes : list = []

    for number in range(x, y + 1):
        if is_prime(number):
            primes.append(number)
    
    return primes



print(find_primes(25, 47))