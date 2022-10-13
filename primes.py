def find_primes(x:int , y:int):
    lst = []

    for i in range(x, y + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                lst.append(i)
    
    for j in lst:
        print(j)



num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))

find_primes(num1,num2)