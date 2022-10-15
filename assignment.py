num1 = int(input("Please entre First number :"))
num2 = int(input("please entre Second number :"))

print("Prime numbers are:")
def find_primes(num1:int , num2:int) -> int:
 for num in range(num1, num2 + 1):
   if num > 1:
    for i in range(2, num):
           if (num % i) == 0:
               break
    else:
            print(num)
           
find_primes(num1,num2)