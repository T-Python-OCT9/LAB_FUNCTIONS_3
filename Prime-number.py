'''# LAB_FUNCTIONS_3


## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

#### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between 25 and 50 are:
29   
31   
37   
41   
43   
47   
'''


first_num =int(input("please inter the first number:\n"))
second_num =int(input("please inter the second number:\n"))


def find_Primes(x, y)->int :
    '''print prime numbers between two parameters by using list'''
    prime_list = []

    for i in range(x, y + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime_list.append(i)

 
    return prime_list



#using loop
def find_Primes2(x,y)->int:
    '''print prime number by using loop'''
    print(f"the primes numbers between {first_num} and {second_num} using loop are:")
    for i in range(x, y + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)

find_Primes2(first_num,second_num)
print(f"the primes numbers between {first_num} and {second_num} using list are:",find_Primes(first_num,second_num))
