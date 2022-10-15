def find_primes(a=int , b=int):
    for i in range (a , b +1):
        if i > 1:
            for j in range(2 , i):
                if (i % j == 0):
                    break
            else:
                print(i)


a = int(input("enter the first num:"))
b = int (input("enter the second num:"))
find_primes(a , b)