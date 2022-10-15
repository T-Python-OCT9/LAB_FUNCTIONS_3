# LAB_FUNCTIONS_3
'''
Create a function : find_primes that takes in 2 parameters of type int , 
and print the prime numbers between the first parameter and the second parameter . 
'''

#### hint
# a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
# Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers 

def find_primes(x : int , y : int) -> int :
    for i in range(x , y + 1):
        if i > 1 :                          # prime numbers are greater than 1 
            for j in range(2 , i):
                if i % j == 0 :             # prime number is divisible only by itself and 1 |
                                            # So if it can be divisible by other numbers it will be not prime
                    #print("it's not a prime number")
                    break
            else: 
                print(i)                    # prime numbers



x = int(input("Enter The First Number : "))
y = int(input("Enter The Second Number : "))
find_primes(x,y)

