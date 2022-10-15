def prime( prime_1 : int, prime_2 : int ):
    for num in range(prime_1,prime_2 + 1):
        if num >= 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)


prime_1 = int(input("Enter number 1 : "))
prime_2 = int(input("Enter lower number 2 : "))

print(prime(prime_1,prime_2))