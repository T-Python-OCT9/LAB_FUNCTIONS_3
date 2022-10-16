''' 
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



def find_primes( inputX:int , inputY:int ) ->int:
    P_list =[]
    for x in range (inputX , inputY+1):# حطيت +١ عشان يطلع للي العدد الاخير 
        if x >1:
            for y in range(2, x):
                if x % y ==0 :
                    break
            else:
               P_list.append(x)
    print(P_list)


inputX =int(input(" first parameter is : "))
inputY =int(input("second parameter is :"))



find_primes(inputX , inputY)