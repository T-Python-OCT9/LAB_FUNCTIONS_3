# LAB_FUNCTIONS_3


# Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter .
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number: "))


def CheckIsPrime(num_1: int, num_2: int) -> int:
    new_list = []
    for i in range(num_1, num_2 + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                new_list.append(i)
    return new_list


print(CheckIsPrime(num_1, num_2))
