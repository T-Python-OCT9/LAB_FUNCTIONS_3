def prime_numbers( prime_1 : int, prime_2 : int ) -> int:
    for Numbers in range(prime_1,prime_2 + 1):
        if Numbers > 1:
            for i in range(2,Numbers):
                if (Numbers % i) == 0:
                    break
            else:
                print(Numbers)


prime_1 = int(input("Please Enter number 1 : "))
prime_2 = int(input("Please Enter another Lower number 2 : "))

print(prime_numbers(prime_1,prime_2))