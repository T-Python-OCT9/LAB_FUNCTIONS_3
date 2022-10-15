def primes_num(num1: int, num2: int) -> int:
    ''' This function takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter'''

    primes_list = []

    for x in range(num1,num2 +1):
        if x > 1:
            for y in range(2, x):
               
                if x % y == 0:
                    break
            else:
                primes_list.append(x)
    print(primes_list)         


user_input1 = int(input("Enter the first int number: "))
user_input2 = int(input("Enter the second inte number: "))

primes_num(num1=user_input1, num2=user_input2)