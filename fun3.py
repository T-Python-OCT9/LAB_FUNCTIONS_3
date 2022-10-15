from re import I

first= int(input("enter the first number .. "))
second=int(input("enter the second number.. "))

def find_primes (first:int , second:int):
    
    for i in range (first,second+1):
        if  (i > 1):
            for b in range (2,i):
                if (i%b == 0):
                    break 
            else:
                print(i)
                
          
find_primes(first,second)

'''We can add the outcomes to list then return the list to print result out of the function'''

