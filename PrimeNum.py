'''
Create a function : find_primes that takes in 2 parameters of type int ,
and print the prime numbers between the first parameter and the second parameter .

'''

def find_primes(num1: int, num2: int) -> int:

    primes_list = []
  
    for x in range(num1,num2 +1):
        if x > 1:
            # prime numbers are greater than 1
            for y in range(2, x):
                #prime numbers can only be divided by 1 and the number itself
                if x % y == 0:
                    break
            else:
                primes_list.append(x)
    print(primes_list)         


user_input1 = int(input("Enter the First integer Number: "))
user_input2 = int(input("Enter the Second integer Number: "))

find_primes(num1=user_input1, num2=user_input2)
