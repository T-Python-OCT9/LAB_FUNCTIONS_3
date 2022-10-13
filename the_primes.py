def the_primes(num1 : int, num2: int) -> int:
    for number in range(num1,num2+1):
        count = 0
        for i in range(1,number+1):
            if number % i == 0:
                count = count + 1
        if count == 2: 
            print(number)
   
the_primes(25,50)

