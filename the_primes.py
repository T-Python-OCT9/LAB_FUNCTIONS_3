def the_primes(num1 : int, num2: int) -> int:
    ''' this function find the primes numbers '''

    for number in range(num1,num2+1): # loop from the num1 to num2
        count : int = 0 # define count to know how many time the number remainder was 0 
        
        for i in range(1,number+1): # loop from 1 to the number 
            if number % i == 0: # chick if the remainder was 0
                count = count + 1 # add 1 to count if the remainder was 0
        
        if count == 2: # chick if count is 2 after looping from 1 to the number
            print(number) 
   
the_primes(25,50)

