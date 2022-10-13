def find_primes(x:int , y:int) ->list:
    print("Primes")
    lst = []

    for i in range(x, y + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                lst.append(i)
    return lst



num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))

for i in find_primes(num1,num2):
    print(i)