def find_primes(first, second) -> int:
     for number in range(first, second):
         if number > 1:
             for i in range(2, number):
              if number % i == 0:
                break
             else:
               print(number)


first = int(input('Enter the first number: '))

second = int(input('Enter the second number: '))

print(find_primes(first,second))