
x = int(input("enter the first number:"))
y = int (input("enter the second number:"))
def find_primes(x=int , y=int):
    for i in range (x , y +1):
        if i > 1:
            for z in range(2 , i):
                if (i % z == 0):
                    break
            else:
                print(i)
find_primes(x , y)

