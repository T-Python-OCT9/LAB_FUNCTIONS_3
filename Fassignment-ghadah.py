# This is the first assignment - ghadah alharbi - 15 oct 


def find_primes (x:int ,y:int ):
    for n in range(x,y+1):
            if n > 1 :
                for v in range(2,n):
                    if n%v==0:
                        break
                else:
                    print(n)
        


find_primes(25,50) 

#or we can take the values from the user find_primes(int(input("enter the lower number ")),int(input("enter the upper number "))) 