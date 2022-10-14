
def find_primes(p1:int , p2:int) -> list:
    if(p1<=1 and p2<=1):
        print("the number shoud be grater than 1 :")
    
    list = []
    x = 2
    for x in range(p1,p2+1):
        for y in range(p1,x):
            if x % y == 0 :
                break
        else:    
            list.append(x)

    return(list)    

  
print(find_primes(2,19))

     

