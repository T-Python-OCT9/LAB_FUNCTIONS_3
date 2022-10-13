# Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter .
def find_primes(first: int, second: int) -> int:
    for number in range(first, second):
        if number > 1:
            for divider in range(2, number):
                if number % divider == 0:
                    break
            else:
                print(number)


find_primes(25, 50)
