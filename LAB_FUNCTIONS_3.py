# LAB LAB_FUNCTIONS_3


def find_primes(first: int, second: int) -> int:
     for number in range(first, second):
         if number > 1:
             for R in range(2, number):
              if number % R == 0:
                break
             else:
               print(number)


find_primes(25, 50)
